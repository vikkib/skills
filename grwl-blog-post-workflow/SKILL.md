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
5.  **Use Contractions Throughout**: The GRWL voice is conversational and warm. Always use contractions in the body copy, subheadings, newsletter, and social posts. For example: "isn't" not "is not", "can't" not "cannot", "shouldn't" not "should not", "you're" not "you are", "it's" not "it is", "don't" not "do not", "we're" not "we are", "that's" not "that is". Avoid formal, stiff phrasing throughout.
6.  **Check for Forbidden Language**: Scrupulously remove any words or phrases from the "Language to Avoid" section of the `brand_guide.md`.

### Step 3: Generate Final Assets and Deliverables

Once the blog post content is finalized, you will generate all the required assets as specified in the `kajabi_checklist.md`.

1.  **Final SEO and Metadata**: Generate the slug, meta title, meta description, and all other required metadata.
2.  **Tag Selection**: Select the single most relevant Kajabi tag for the post from this list:
    - `food & mood`
    - `food facts`
    - `food finds`
    - `get moving`
    - `mental & emotional weight`
    - `recipe`
    - `mindset`

    Choose the tag that best reflects the post's primary focus. If the post spans multiple categories, pick the dominant one. Include the selected tag in the deliverables with a one-sentence rationale.
3.  **Image Generation**: Generate all three required images as specified in the `kajabi_checklist.md` Visuals section: a wide featured image (`landscape`) for the top of the post, a wide mid-post image (`landscape`) placed between the third and fourth H2 sections, and a tall closing image (`portrait`) placed just above or alongside the final CTA. Write alt text for each. Vary the woman's ethnicity across the three images within the same post.
4.  **Callout Box**: Write a short, punchy callout box statement (1-2 sentences max) that captures the emotional core of the post, followed by a brief CTA (one sentence). The statement should feel bold and quotable -- something a reader would stop and re-read. The CTA should link to the GRWL program or a related resource. Use contractions. Do not use em dashes.
5.  **Newsletter and Social Media Content**: Write the newsletter summary and social media posts as specified in the checklist.
6.  **Final Review**: Perform a final check of all deliverables against the `kajabi_checklist.md`. Ensure the Flesch-Kincaid score is 65+.

### Step 4: Package and Deliver

Organize all the final deliverables into two files:

1.  **Blog post file** (`final_post.md`): The rewritten blog post in Markdown format. This is fine as a .md file since it is not pasted into Kajabi directly.

2.  **Deliverables file** (`deliverables.txt`): MUST be saved as a plain .txt file -- NOT Markdown (.md). This is critical. The user copies content from this file directly into Kajabi templates. Markdown files rendered in the Manus conversation UI carry hidden CSS that breaks Kajabi's text blocks. The .txt file must contain:
    - Selected Kajabi tag and rationale
    - All SEO and metadata elements
    - Callout box statement and CTA
    - Featured image alt text
    - Newsletter content (subject, headline, preview text, intro paragraph, blog summary with CTA)
    - Facebook and Instagram social posts with hashtags

    Use plain section headers (e.g. ALL CAPS with dashes underneath) instead of Markdown syntax. Use only straight quotes and plain hyphens. No asterisks, pound signs, or other Markdown characters.

Attach both files when presenting to the user.
