# 4. How ChatGPT and AI Search Work

## A. Ordinary search engine
1. A user enters keywords or a question.
2. The search system interprets the query and consults an index of webpages/documents.
3. It retrieves candidate results and ranks them using relevance and other signals.
4. It displays links/snippets; the user opens and verifies the original sources.

A search engine is primarily retrieving and ranking existing documents. It is not the same thing as a language model writing a new answer.

## B. Large language model (LLM)
1. **Input processing:** The prompt and conversation context are converted into tokens. A token can be a word, part of a word, punctuation or another text unit.
2. **Numerical representation:** Tokens are represented numerically. Transformer models use contextual computations, including attention, to represent relationships between tokens.
3. **Context processing:** The model processes the prompt in light of learned parameters and available context.
4. **Generation:** The model predicts output tokens step by step until the answer is complete or a stopping condition is reached.

An LLM can generate plausible text that is incorrect. Important claims should be checked against original sources.

## C. Semantic search and embeddings
- An **embedding** is a numeric vector representing a piece of text.
- Semantic search compares the vector for a query with vectors for documents, often using a similarity measure.
- It can retrieve conceptually related material even when the query and document do not use exactly the same words.
- Embedding similarity is not proof that a result is true or authoritative.

## D. Retrieval-Augmented Generation (RAG)
A typical RAG workflow is:

**Question → retrieve relevant documents → provide selected text as context → LLM generates a grounded response → cite/check sources.**

RAG can make answers more source-grounded, but retrieval can miss relevant documents and the model can still misinterpret evidence. Citations should be opened and checked.

## E. What happens when asking ChatGPT to research a paper?
Depending on the product and tools enabled, the system may answer from its trained model, search the web, inspect provided files, or retrieve passages from connected sources. Not every ChatGPT question triggers a web search. A reliable research workflow is:
1. Find the paper through Google Scholar or a publisher/index.
2. Verify the DOI and publication metadata.
3. Open the full paper, not only a search snippet.
4. Check the five required sections.
5. Use AI to explain difficult language or draft a summary.
6. Compare every factual statement with the paper and cite it accurately.

## F. Suggested diagram for class notes
```text
Question
   |
Tokenization and context
   |
Search/retrieval (only if used) ----> Original documents
   |                                      |
   +--------------- relevant context <----+
   |
LLM processes context and generates output
   |
Human verifies claims against original sources
```

## G. Research questions to explore
- How does tokenization differ from word matching?
- What is the difference between lexical search and semantic search?
- What are embeddings and cosine similarity?
- What does transformer attention do at a high level?
- What is RAG, and why does it need source verification?
- What are hallucination, prompt injection and retrieval errors?

## Source note
This section is a general technical explanation, not a summary of a single research paper. Add authoritative AI/IR references if the lecturer expects formal citations for this part.
