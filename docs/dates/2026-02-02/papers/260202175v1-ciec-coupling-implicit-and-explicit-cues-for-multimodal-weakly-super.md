---
layout: default
title: CIEC: Coupling Implicit and Explicit Cues for Multimodal Weakly Supervised Manipulation Localization
---

# CIEC: Coupling Implicit and Explicit Cues for Multimodal Weakly Supervised Manipulation Localization
**arXiv**：[2602.02175v1](https://arxiv.org/abs/2602.02175) · [PDF](https://arxiv.org/pdf/2602.02175.pdf)  
**作者**：Xinquan Yu, Wei Lu, Xiangyang Luo  

**一句话要点**：提出CIEC框架，通过耦合隐式和显式线索实现多模态弱监督篡改定位，仅需粗粒度标注。

**关键词**：多模态篡改定位, 弱监督学习, 隐式显式线索耦合, 文本引导视觉定位, 视觉偏差文本校准

## 3 点简述
- 核心问题：多模态篡改定位依赖细粒度标注，成本高且耗时，需弱监督方法。
- 方法要点：设计TRPS模块基于文本引导锁定视觉可疑区域，VCTG模块利用视觉偏差校准文本定位。
- 实验或效果：在多个评估指标上达到与全监督方法可比的结果，验证了有效性。

## 摘要（原文）

> To mitigate the threat of misinformation, multimodal manipulation localization has garnered growing attention. Consider that current methods rely on costly and time-consuming fine-grained annotations, such as patch/token-level annotations. This paper proposes a novel framework named Coupling Implicit and Explicit Cues (CIEC), which aims to achieve multimodal weakly-supervised manipulation localization for image-text pairs utilizing only coarse-grained image/sentence-level annotations. It comprises two branches, image-based and text-based weakly-supervised localization. For the former, we devise the Textual-guidance Refine Patch Selection (TRPS) module. It integrates forgery cues from both visual and textual perspectives to lock onto suspicious regions aided by spatial priors. Followed by the background silencing and spatial contrast constraints to suppress interference from irrelevant areas. For the latter, we devise the Visual-deviation Calibrated Token Grounding (VCTG) module. It focuses on meaningful content words and leverages relative visual bias to assist token localization. Followed by the asymmetric sparse and semantic consistency constraints to mitigate label noise and ensure reliability. Extensive experiments demonstrate the effectiveness of our CIEC, yielding results comparable to fully supervised methods on several evaluation metrics.

