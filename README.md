# PDF to Flare XHTML Conversion
This repo provides resources for converting a collection of PDFs into MadCap Flare's XHTML format. This is the best way I could find to get PDFs into Flare quickly without too much manual cleanup.

I think people will find this helpful, but I have not had much time to describe this process in detail. Please [submit an issue](https://github.com/samegel/pdf-convert-demo/issues) if you'd like more detailed documentation about this process.

## How it works
Hopefully this brief explanation will give you an idea how to use the scripts in this folder to convert PDF to Flare format.

You should obviously check to make sure this will work for your situation, and make modifications as necessary.

1. Gather PDFs to convert into one folder.
2. In Adobe DC, automatically remove the cover page from all PDFs in the folder using the [Adobe Action Wizard](https://helpx.adobe.com/acrobat/using/action-wizard-acrobat-pro.html) and this script: `Content/Scripts/Batch_Remove_First_Page.sequ`.
3. In Adobe DC, automatically convert all PDFs to HTML using `Content/Scripts/PDF_to_HTML.sequ`. 
4. Process HTML into XHTML using this script: `Content/Scripts/adobedc-html2xhtml.py`. This script removes markup from the Adobe DC HTML conversion that is unnecessary for my purposes, including id, style, and class attributes from every element.
5. Clean up XHTML output in Flare as necessary. For example, this process produces one XHTML topic for every PDF, and you will probably want to break the XHTML file into smaller topics to help enable content reuse.
