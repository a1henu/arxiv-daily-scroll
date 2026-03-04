---
layout: default
title: LLandMark: A Multi-Agent Framework for Landmark-Aware Multimodal Interactive Video Retrieval
---

# LLandMark: A Multi-Agent Framework for Landmark-Aware Multimodal Interactive Video Retrieval
**arXiv**：[2603.02888v1](https://arxiv.org/abs/2603.02888) · [PDF](https://arxiv.org/pdf/2603.02888.pdf)  
**作者**：Minh-Chi Phung, Thien-Bao Le, Cam-Tu Tran-Thi, Thu-Dieu Nguyen-Thi, Vu-Hung Dao  

**一句话要点**：提出LLandMark多智能体框架，用于基于地标的多模态交互式视频检索，以处理复杂查询。

**关键词**：多模态视频检索, 多智能体框架, 地标推理, CLIP语义匹配, LLM辅助管道, 越南文本识别

## 3 点简述
- 核心问题：视频数据多样化和规模化要求检索系统具备多模态理解、自适应推理和领域知识集成能力。
- 方法要点：采用模块化多智能体协作，包括查询解析、地标推理、多模态检索和答案合成，并引入LLM辅助图像到图像管道。
- 实验或效果：实验显示LLandMark实现自适应、文化基础和可解释的检索性能，提升越南场景的语义匹配。

## 摘要（原文）

> The increasing diversity and scale of video data demand retrieval systems capable of multimodal understanding, adaptive reasoning, and domain-specific knowledge integration. This paper presents LLandMark, a modular multi-agent framework for landmark-aware multimodal video retrieval to handle real-world complex queries. The framework features specialized agents that collaborate across four stages: query parsing and planning, landmark reasoning, multimodal retrieval, and reranked answer synthesis. A key component, the Landmark Knowledge Agent, detects cultural or spatial landmarks and reformulates them into descriptive visual prompts, enhancing CLIP-based semantic matching for Vietnamese scenes. To expand capabilities, we introduce an LLM-assisted image-to-image pipeline, where a large language model (Gemini 2.5 Flash) autonomously detects landmarks, generates image search queries, retrieves representative images, and performs CLIP-based visual similarity matching, removing the need for manual image input. In addition, an OCR refinement module leveraging Gemini and LlamaIndex improves Vietnamese text recognition. Experimental results show that LLandMark achieves adaptive, culturally grounded, and explainable retrieval performance.

