---
layout: default
title: DIVER: Dynamic Iterative Visual Evidence Reasoning for Multimodal Fake News Detection
---

# DIVER: Dynamic Iterative Visual Evidence Reasoning for Multimodal Fake News Detection
**arXiv**：[2601.07178v1](https://arxiv.org/abs/2601.07178) · [PDF](https://arxiv.org/pdf/2601.07178.pdf)  
**作者**：Weilin Zhou, Zonghao Ying, Chunlei Meng, Jiahui Liu, Hengyang Zhou, Quanchen Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  

**一句话要点**：提出DIVER框架以解决多模态假新闻检测中的计算冗余和幻觉风险问题。

**关键词**：多模态假新闻检测, 动态迭代推理, 视觉证据对齐, 不确定性感知融合, 细粒度视觉工具

## 3 点简述
- 核心问题：现有方法依赖静态融合或大语言模型，存在视觉基础弱导致的冗余和幻觉风险。
- 方法要点：采用渐进式证据驱动推理，先文本分析，不足时引入视觉信息，自适应对齐验证和细粒度工具提取证据。
- 实验或效果：在Weibo等数据集上平均性能提升2.72%，推理延迟减少4.12秒。

## 摘要（原文）

> Multimodal fake news detection is crucial for mitigating adversarial misinformation. Existing methods, relying on static fusion or LLMs, face computational redundancy and hallucination risks due to weak visual foundations. To address this, we propose DIVER (Dynamic Iterative Visual Evidence Reasoning), a framework grounded in a progressive, evidence-driven reasoning paradigm. DIVER first establishes a strong text-based baseline through language analysis, leveraging intra-modal consistency to filter unreliable or hallucinated claims. Only when textual evidence is insufficient does the framework introduce visual information, where inter-modal alignment verification adaptively determines whether deeper visual inspection is necessary. For samples exhibiting significant cross-modal semantic discrepancies, DIVER selectively invokes fine-grained visual tools (e.g., OCR and dense captioning) to extract task-relevant evidence, which is iteratively aggregated via uncertainty-aware fusion to refine multimodal reasoning. Experiments on Weibo, Weibo21, and GossipCop demonstrate that DIVER outperforms state-of-the-art baselines by an average of 2.72\%, while optimizing inference efficiency with a reduced latency of 4.12 s.

