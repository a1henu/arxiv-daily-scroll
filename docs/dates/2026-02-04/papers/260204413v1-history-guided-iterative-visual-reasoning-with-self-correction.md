---
layout: default
title: History-Guided Iterative Visual Reasoning with Self-Correction
---

# History-Guided Iterative Visual Reasoning with Self-Correction
**arXiv**：[2602.04413v1](https://arxiv.org/abs/2602.04413) · [PDF](https://arxiv.org/pdf/2602.04413.pdf)  
**作者**：Xinglong Yang, Zhilin Peng, Zhanzhan Liu, Haochen Shi, Sheng-Jun Huang  

**一句话要点**：提出H-GIVR框架以解决多模态大语言模型在迭代推理中无法动态纠错的问题

**关键词**：多模态大语言模型, 视觉推理, 自一致性方法, 迭代推理, 动态纠错, 跨模态任务

## 3 点简述
- 现有自一致性方法依赖固定采样投票，未重用历史信息，导致视觉理解错误难以主动纠正
- H-GIVR框架通过多次观察图像并参考历史答案，实现动态错误校正，提升推理准确性
- 在五个数据集和三个模型上实验，显著提高跨模态推理精度，同时保持低计算成本

## 摘要（原文）

> Self-consistency methods are the core technique for improving the reasoning reliability of multimodal large language models (MLLMs). By generating multiple reasoning results through repeated sampling and selecting the best answer via voting, they play an important role in cross-modal tasks. However, most existing self-consistency methods are limited to a fixed ``repeated sampling and voting'' paradigm and do not reuse historical reasoning information. As a result, models struggle to actively correct visual understanding errors and dynamically adjust their reasoning during iteration. Inspired by the human reasoning behavior of repeated verification and dynamic error correction, we propose the H-GIVR framework. During iterative reasoning, the MLLM observes the image multiple times and uses previously generated answers as references for subsequent steps, enabling dynamic correction of errors and improving answer accuracy. We conduct comprehensive experiments on five datasets and three models. The results show that the H-GIVR framework can significantly improve cross-modal reasoning accuracy while maintaining low computational cost. For instance, using \texttt{Llama3.2-vision:11b} on the ScienceQA dataset, the model requires an average of 2.57 responses per question to achieve an accuracy of 78.90\%, representing a 107\% improvement over the baseline.

