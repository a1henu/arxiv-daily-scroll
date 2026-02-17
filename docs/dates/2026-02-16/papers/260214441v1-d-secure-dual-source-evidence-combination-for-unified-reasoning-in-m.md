---
layout: default
title: D-SECURE: Dual-Source Evidence Combination for Unified Reasoning in Misinformation Detection
---

# D-SECURE: Dual-Source Evidence Combination for Unified Reasoning in Misinformation Detection
**arXiv**：[2602.14441v1](https://arxiv.org/abs/2602.14441) · [PDF](https://arxiv.org/pdf/2602.14441.pdf)  
**作者**：Gagandeep Singh, Samudi Amarasinghe, Priyanka Singh  

**一句话要点**：提出D-SECURE框架，结合内部篡改检测与外部证据推理以解决多模态虚假信息检测问题。

**关键词**：多模态虚假信息检测, 篡改检测, 证据检索, 融合推理, 可解释性

## 3 点简述
- 核心问题：多模态虚假信息混合逼真图像编辑与误导文本，现有单源系统易漏检内部一致伪造或外部证据验证的篡改。
- 方法要点：集成HAMMER篡改检测器与DEFAME检索管道，先进行广泛验证，再分析残留或不确定案例的细粒度编辑。
- 实验或效果：在DGM4和ClaimReview数据集上实验，展示两种系统的互补优势，并提供统一可解释报告。

## 摘要（原文）

> Multimodal misinformation increasingly mixes realistic im-age edits with fluent but misleading text, producing persuasive posts that are difficult to verify. Existing systems usually rely on a single evidence source. Content-based detectors identify local inconsistencies within an image and its caption but cannot determine global factual truth. Retrieval-based fact-checkers reason over external evidence but treat inputs as coarse claims and often miss subtle visual or textual manipulations. This separation creates failure cases where internally consistent fabrications bypass manipulation detectors and fact-checkers verify claims that contain pixel-level or token-level corruption. We present D-SECURE, a framework that combines internal manipulation detection with external evidence-based reasoning for news-style posts. D-SECURE integrates the HAMMER manipulation detector with the DEFAME retrieval pipeline. DEFAME performs broad verification, and HAMMER analyses residual or uncertain cases that may contain fine-grained edits. Experiments on DGM4 and ClaimReview samples highlight the complementary strengths of both systems and motivate their fusion. We provide a unified, explainable report that incorporates manipulation cues and external evidence.

