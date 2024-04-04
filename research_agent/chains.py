from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_openai import ChatOpenAI
from prompts import REPORT_PROMPT, SEARCH_PROMPT, SUMMARY_PROMPT
from utils import collapse_list_of_lists, scrape_text, web_search

search_question_chain = (
    SEARCH_PROMPT | ChatOpenAI(temperature=0) | JsonOutputParser()
)

scrape_and_summarize_chain = RunnablePassthrough.assign(
    summary=RunnablePassthrough.assign(
        text=lambda x: scrape_text(x["url"])[:10000]
    )
    | SUMMARY_PROMPT
    | ChatOpenAI(model="gpt-3.5-turbo-1106")
    | StrOutputParser()
) | (lambda x: f"URL: {x['url']}\n\nSUMMARY: {x['summary']}")


web_search_chain = (
    RunnablePassthrough.assign(urls=lambda x: web_search(x["question"]))
    | (lambda x: [{"question": x["question"], "url": u} for u in x["urls"]])
    | scrape_and_summarize_chain.map()
)

full_research_chain = (
    search_question_chain
    | (lambda x: [{"question": q} for q in x])
    | web_search_chain.map()
)


full_chain = (
    RunnablePassthrough.assign(
        research_summary=full_research_chain | collapse_list_of_lists
    )
    | REPORT_PROMPT
    | ChatOpenAI(model="gpt-3.5-turbo-1106")
    | StrOutputParser()
)
