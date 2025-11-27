---
layout: default
title: GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision
---

# GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision
**arXiv**：[2511.20994v1](https://arxiv.org/abs/2511.20994) · [PDF](https://arxiv.org/pdf/2511.20994.pdf)  
**作者**：Yuxiao Xiang, Junchi Chen, Zhenchao Jin, Changtao Miao, Haojie Yuan, Qi Chu, Tao Gong, Nenghai Yu  

**一句话要点**：提出GuardTrace-VL以检测多模态推理中的不安全内容

**关键词**：多模态安全检测, 推理过程监控, 渐进式训练, 图像-文本分析, 安全数据集构建

## 3 点简述
- 多模态大推理模型在推理过程中可能产生不安全内容，现有方法仅评估输入和最终答案
- 通过联合图像-文本分析监控完整推理管道，并采用渐进式训练方案学习安全偏好
- 在测试集上F1分数达93.1%，比先前方法提升13.5%

## 摘要（原文）

> Multimodal large reasoning models (MLRMs) are increasingly deployed for vision-language tasks that produce explicit intermediate rationales. However, reasoning traces can contain unsafe content even when the final answer is non-harmful, creating deployment risks. Existing multimodal safety guards primarily evaluate only the input question and the final answer, neglecting the intermediate reasoning process. This oversight allows undetected harm, such as biased inferences or policy-violating use of visual context, to emerge during reasoning. We introduce GuardTrace-VL, a vision-aware safety auditor that monitors the full Question-Thinking-Answer (QTA) pipeline via joint image-text analysis, enabling detection of unsafe content as it emerges in the reasoning stage. To support training and evaluation, we construct the GuardTrace dataset, which is generated through diverse prompting strategies and refined via a MLRM- and human-based voting and verification pipeline. Furthermore, we propose a three-stage progressive training scheme combined with the data refinement process, enabling the model to learn nuanced and context-dependent safety preferences according to different risk levels. On our proposed test set covering both in-domain and out-of-domain scenarios, GuardTrace-VL model achieves an F1 score of 93.1% on unsafe reasoning detection tasks, representing a 13.5% improvement in F1 score compared to the previous strongest multimodal safety defense methods. The codes will be made publicly available.

