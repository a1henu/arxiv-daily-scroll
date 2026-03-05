---
layout: default
title: Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning
---

# Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning
**arXiv**：[2603.03752v1](https://arxiv.org/abs/2603.03752) · [PDF](https://arxiv.org/pdf/2603.03752.pdf)  
**作者**：Chuang Zhang, Zizhen Zhu, Yihao Wei, Bing Tian, Junyi Liu, Henan Wang, Xavier Wang, Yaxiao Liu  

**一句话要点**：提出COREA系统，通过小大语言模型协作与置信度校准，在复杂推理任务中平衡准确性与成本。

**关键词**：语言模型协作, 置信度校准, 成本效率, 强化学习, 推理任务

## 3 点简述
- 核心问题：大语言模型推理能力强但成本高，小语言模型成本低但准确性不足。
- 方法要点：使用小模型先尝试回答并输出置信度，低置信度问题转交大模型处理，通过强化学习校准置信度。
- 实验或效果：在数学与非数学数据集上，相比单独使用大模型，成本降低16.8%-21.5%，准确率下降小于2%。

## 摘要（原文）

> Large language models (LLMs) demonstrate superior reasoning capabilities compared to small language models (SLMs), but incur substantially higher costs. We propose COllaborative REAsoner (COREA), a system that cascades an SLM with an LLM to achieve a balance between accuracy and cost in complex reasoning tasks. COREA first attempts to answer questions using the SLM, which outputs both an answer and a verbalized confidence score. Questions with confidence below a predefined threshold are deferred to the LLM for more accurate resolution. We introduce a reinforcement learning-based training algorithm that aligns the SLM's confidence through an additional confidence calibration reward. Extensive experiments demonstrate that our method jointly improves the SLM's reasoning ability and confidence calibration across diverse datasets and model backbones. Compared to using the LLM alone, COREA reduces cost by 21.5% and 16.8% on out-of-domain math and non-math datasets, respectively, with only an absolute pass@1 drop within 2%.

