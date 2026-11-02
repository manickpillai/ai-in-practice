# Limitations

[← Back to README](../README.md)

- The index only holds h1-h3 headings; h4 and deeper are not indexed. If a section's useful content isn't reflected in its heading, the skill can miss it.
- Matching is done by the model reading `llms.txt`, not by a search engine. That works for small docs but won't scale to hundreds of pages without a bigger index.
- Anchors are generated to match MkDocs' default slugs. Custom heading ids or duplicate headings on one page can produce wrong links.
- Links are local markdown paths, not published site URLs.
- The sample docs are generic. Quality of answers depends entirely on the quality of the docs.
