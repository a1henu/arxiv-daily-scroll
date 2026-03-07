---
layout: default
title: Are Multimodal LLMs Ready for Surveillance? A Reality Check on Zero-Shot Anomaly Detection in the Wild
---

# Are Multimodal LLMs Ready for Surveillance? A Reality Check on Zero-Shot Anomaly Detection in the Wild
**arXiv**：[2603.04727v1](https://arxiv.org/abs/2603.04727) · [PDF](https://arxiv.org/pdf/2603.04727.pdf)  
**作者**：Shanle Yao, Armin Danesh Pazho, Narges Rashvand, Hamed Tabkhi  

**一句话要点**：评估多模态大语言模型在零样本视频异常检测中的性能，揭示保守偏差与召回瓶颈

**关键词**：多模态大语言模型, 视频异常检测, 零样本学习, 语言引导推理, 保守偏差, 召回瓶颈

## 3 点简述
- 核心问题：多模态大语言模型在真实世界视频异常检测中的可靠性未知，需评估其零样本性能。
- 方法要点：将异常检测重构为语言引导的二元分类任务，研究提示特异性和时间窗口长度的影响。
- 实验或效果：模型在零样本设置下表现出保守偏差，高精度但召回崩溃；类特定指令可提升F1分数，但召回仍是关键瓶颈。

## 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated impressive general competence in video understanding, yet their reliability for real-world Video Anomaly Detection (VAD) remains largely unexplored. Unlike conventional pipelines relying on reconstruction or pose-based cues, MLLMs enable a paradigm shift: treating anomaly detection as a language-guided reasoning task. In this work, we systematically evaluate state-of-the-art MLLMs on the ShanghaiTech and CHAD benchmarks by reformulating VAD as a binary classification task under weak temporal supervision. We investigate how prompt specificity and temporal window lengths (1s--3s) influence performance, focusing on the precision--recall trade-off. Our findings reveal a pronounced conservative bias in zero-shot settings; while models exhibit high confidence, they disproportionately favor the 'normal' class, resulting in high precision but a recall collapse that limits practical utility. We demonstrate that class-specific instructions can significantly shift this decision boundary, improving the peak F1-score on ShanghaiTech from 0.09 to 0.64, yet recall remains a critical bottleneck. These results highlight a significant performance gap for MLLMs in noisy environments and provide a foundation for future work in recall-oriented prompting and model calibration for open-world surveillance, which demands complex video understanding and reasoning.

