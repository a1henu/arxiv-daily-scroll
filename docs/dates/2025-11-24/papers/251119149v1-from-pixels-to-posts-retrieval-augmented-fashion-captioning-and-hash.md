---
layout: default
title: From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation
---

# From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation
**arXiv**：[2511.19149v1](https://arxiv.org/abs/2511.19149) · [PDF](https://arxiv.org/pdf/2511.19149.pdf)  
**作者**：Moazzam Umer Gondal, Hamad Ul Qudous, Daniya Siddiqui, Asma Ahmad Farhan  

**一句话要点**：提出检索增强框架以解决时尚图像描述和标签生成中的属性保真度与泛化问题

**关键词**：检索增强生成, 时尚图像描述, 多服装检测, 属性推理, LLM提示, 事实证据包

## 3 点简述
- 核心问题：端到端方法在时尚图像描述中属性保真度低、领域泛化差，易产生幻觉。
- 方法要点：结合多服装检测、属性推理和LLM提示，构建事实证据包指导文本生成。
- 实验或效果：RAG-LLM在属性覆盖率达0.80，优于BLIP，减少幻觉，提升可扩展性。

## 摘要（原文）

> This paper introduces the retrieval-augmented framework for automatic fashion caption and hashtag generation, combining multi-garment detection, attribute reasoning, and Large Language Model (LLM) prompting. The system aims to produce visually grounded, descriptive, and stylistically interesting text for fashion imagery, overcoming the limitations of end-to-end captioners that have problems with attribute fidelity and domain generalization. The pipeline combines a YOLO-based detector for multi-garment localization, k-means clustering for dominant color extraction, and a CLIP-FAISS retrieval module for fabric and gender attribute inference based on a structured product index. These attributes, together with retrieved style examples, create a factual evidence pack that is used to guide an LLM to generate human-like captions and contextually rich hashtags. A fine-tuned BLIP model is used as a supervised baseline model for comparison. Experimental results show that the YOLO detector is able to obtain a mean Average Precision (mAP@0.5) of 0.71 for nine categories of garments. The RAG-LLM pipeline generates expressive attribute-aligned captions and achieves mean attribute coverage of 0.80 with full coverage at the 50% threshold in hashtag generation, whereas BLIP gives higher lexical overlap and lower generalization. The retrieval-augmented approach exhibits better factual grounding, less hallucination, and great potential for scalable deployment in various clothing domains. These results demonstrate the use of retrieval-augmented generation as an effective and interpretable paradigm for automated and visually grounded fashion content generation.

