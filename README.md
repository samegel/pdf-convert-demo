# PDF to Flare XHTML Conversion demo.
1. Gather PDFs to convert.
2. In Adobe DC, remove the cover page from all PDFs that have a cover page using `Batch_Remove_First_Page.sequ`
3. In Adobe DC, convert all PDFs to HTML using `PDF_to_HTML.sequ`
4. Process HTML into XHTML using script (including removing the DC-output id, style, and class attributes from every element).
5. Clean up XHTML output in Flare (such as reflowing text/images where appropriate and removing footer content from topics).
