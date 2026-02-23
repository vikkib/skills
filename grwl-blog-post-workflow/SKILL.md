---
name: grwl-blog-post-workflow
description: A comprehensive workflow for transforming a draft blog post into a polished, on-brand, and SEO/AEO/GIO-optimized Kajabi blog post for the Get Real Weight Loss (GRWL) client.
---

# GRWL Blog Post Workflow

This skill provides a complete, step-by-step workflow for taking a draft blog post and turning it into a final, client-ready asset that aligns with the Get Real Weight Loss (GRWL) brand guidelines. This includes content transformation, SEO/AEO/GIO optimization, asset creation, and generation of related promotional content.

## Core Principle: Adherence to Brand and Checklists

This workflow is designed to be followed precisely. The GRWL brand is highly specific, and consistency is key. There are two critical reference documents that you MUST read and follow:

*   `/home/ubuntu/skills/grwl-blog-post-workflow/references/brand_guide.md`: The complete guide to the GRWL brand voice, tone, visual style, and language to use and avoid.
*   `/home/ubuntu/skills/grwl-blog-post-workflow/references/kajabi_checklist.md`: A detailed, step-by-step checklist for every part of the blog post creation and delivery process.

**Do not proceed without first reading both of these documents.**

## The Workflow

This is a sequential process. Follow these steps in order.

### Step 1: Ingest and Analyze the Draft

1.  **Receive the draft blog post** from the user. It will typically be a Markdown file.
2.  **Read the draft** to understand its core message and structure.
3.  **Analyze the draft** against the GRWL brand guidelines. Use the analysis scripts provided to get a baseline:

    ```bash
    # Check for keywords (replace with keywords from the draft or user)
    python3.11 /home/ubuntu/skills/grwl-blog-post-workflow/scripts/keyword_checker.py <draft_file_path> <keyword1> <keyword2> ...

    # Calculate readability score
    python3.11 /home/ubuntu/skills/grwl-blog-post-workflow/scripts/calculate_readability.py <draft_file_path>

    # Lint for prose style
    python3.11 /home/ubuntu/skills/grwl-blog-post-workflow/scripts/style_linter.py <draft_file_path>
    ```

### Step 2: Rewrite and Refine the Content

This is the most critical step. You will now rewrite the draft to align with the GRWL brand and the Kajabi checklist.

1.  **Apply the GRWL Voice and Tone**: Rewrite sentences and paragraphs to be warm, supportive, and shame-free. Infuse the personality of the brand personas (Oprah, Mel Robbins, etc.) as described in the `brand_guide.md`.
2.  **Incorporate Keywords**: Naturally weave the primary keyword (and any secondary keywords) into the title, subheadings, and body text. Aim for a keyword density of 1-3%.
3.  **Structure the Post**: Follow the Kajabi blog structure precisely: Hook, optional personal tie-in, 3-6 main sections with H2s, solution/insight section, and a clear CTA.
4.  **Formatting for Readability**: Keep paragraphs short (2-4 lines), use bolding for emphasis, and ensure you are not using em-dashes. Follow all formatting rules in the `kajabi_checklist.md`.
5.  **Check for Forbidden Language**: Scrupulously remove any words or phrases from the "Language to Avoid" section of the `brand_guide.md`.

### Step 3: Generate Final Assets and Deliverables

Once the blog post content is finalized, you will generate all the required assets as specified in the `kajabi_checklist.md`.

1.  **Final SEO and Metadata**: Generate the slug, meta title, meta description, and all other required metadata.
2.  **Image Generation**: Create a prompt for the featured image that aligns with the visual style in the `brand_guide.md`. Generate the image, and write the alt text.
3.  **Newsletter and Social Media Content**: Write the newsletter summary and social media posts as specified in the checklist.
4.  **Final Review**: Perform a final check of all deliverables against the `kajabi_checklist.md`. Ensure the Flesch-Kincaid score is 65+.

### Step 4: Package and Deliver

Organize all the final deliverables into a clear, easy-to-understand format for the user. This should include:

*   The final, rewritten blog post in a Markdown file.
*   All the metadata and SEO elements.
*   The generated image and its alt text.
*   The newsletter content.
*   The social media posts.

Present these to the user as a complete package.
