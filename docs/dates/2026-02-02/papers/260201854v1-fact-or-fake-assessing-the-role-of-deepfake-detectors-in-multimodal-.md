---
layout: default
title: Fact or Fake? Assessing the Role of Deepfake Detectors in Multimodal Misinformation Detection
---

# Fact or Fake? Assessing the Role of Deepfake Detectors in Multimodal Misinformation Detection
**arXiv**：[2602.01854v1](https://arxiv.org/abs/2602.01854) · [PDF](https://arxiv.org/pdf/2602.01854.pdf)  
**作者**：A S M Sharifuzzaman Sagar, Mohammed Bennamoun, Farid Boussaid, Naeha Sharif, Lian Xu, Shaaban Sahmoud, Ali Kishk  

**一句话要点**：评估深度伪造检测器在多模态虚假信息检测中的作用，发现其贡献有限且可能降低性能。

**关键词**：多模态虚假信息检测, 深度伪造检测器, 事实核查系统, 语义理解, 外部证据, 性能评估

## 3 点简述
- 核心问题：深度伪造检测器是否有助于验证图像-文本声明的真实性，还是引入误导性先验？
- 方法要点：系统分析深度伪造检测器，结合证据驱动的事实核查系统与混合系统进行评估。
- 实验或效果：深度伪造检测器F1分数较低，融入事实核查管道会降低性能，证据驱动系统表现最佳。

## 摘要（原文）

> In multimodal misinformation, deception usually arises not just from pixel-level manipulations in an image, but from the semantic and contextual claim jointly expressed by the image-text pair. Yet most deepfake detectors, engineered to detect pixel-level forgeries, do not account for claim-level meaning, despite their growing integration in automated fact-checking (AFC) pipelines. This raises a central scientific and practical question: Do pixel-level detectors contribute useful signal for verifying image-text claims, or do they instead introduce misleading authenticity priors that undermine evidence-based reasoning? We provide the first systematic analysis of deepfake detectors in the context of multimodal misinformation detection. Using two complementary benchmarks, MMFakeBench and DGM4, we evaluate: (1) state-of-the-art image-only deepfake detectors, (2) an evidence-driven fact-checking system that performs tool-guided retrieval via Monte Carlo Tree Search (MCTS) and engages in deliberative inference through Multi-Agent Debate (MAD), and (3) a hybrid fact-checking system that injects detector outputs as auxiliary evidence. Results across both benchmark datasets show that deepfake detectors offer limited standalone value, achieving F1 scores in the range of 0.26-0.53 on MMFakeBench and 0.33-0.49 on DGM4, and that incorporating their predictions into fact-checking pipelines consistently reduces performance by 0.04-0.08 F1 due to non-causal authenticity assumptions. In contrast, the evidence-centric fact-checking system achieves the highest performance, reaching F1 scores of approximately 0.81 on MMFakeBench and 0.55 on DGM4. Overall, our findings demonstrate that multimodal claim verification is driven primarily by semantic understanding and external evidence, and that pixel-level artifact signals do not reliably enhance reasoning over real-world image-text misinformation.

