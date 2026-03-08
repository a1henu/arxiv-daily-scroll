---
layout: default
title: Beyond Word Error Rate: Auditing the Diversity Tax in Speech Recognition through Dataset Cartography
---

# Beyond Word Error Rate: Auditing the Diversity Tax in Speech Recognition through Dataset Cartography
**arXiv**：[2603.05267v1](https://arxiv.org/abs/2603.05267) · [PDF](https://arxiv.org/pdf/2603.05267.pdf)  
**作者**：Ting-Hui Cheng, Line H. Clemmensen, Sneha Das  

**一句话要点**：提出样本难度指数以审计语音识别中的多样性税，超越词错误率评估。

**关键词**：语音识别审计, 多样性税, 样本难度指数, 语义评估指标, 数据制图, 模型偏见

## 3 点简述
- 核心问题：词错误率无法捕捉语义保真度，掩盖了对边缘化说话者的系统性识别失败。
- 方法要点：引入样本难度指数，量化人口和声学因素如何驱动模型失败，并评估非线性语义指标。
- 实验或效果：通过数据制图展示EmbER和SemDist指标暴露WER忽略的隐藏偏见和模型分歧。

## 摘要（原文）

> Automatic speech recognition (ASR) systems are predominantly evaluated using the Word Error Rate (WER). However, raw token-level metrics fail to capture semantic fidelity and routinely obscures the `diversity tax', the disproportionate burden on marginalized and atypical speaker due to systematic recognition failures. In this paper, we explore the limitations of relying solely on lexical counts by systematically evaluating a broader class of non-linear and semantic metrics. To enable rigorous model auditing, we introduce the sample difficulty index (SDI), a novel metric that quantifies how intrinsic demographic and acoustic factors drive model failure. By mapping SDI on data cartography, we demonstrate that metrics EmbER and SemDist expose hidden systemic biases and inter-model disagreements that WER ignores. Finally, our findings are the first steps towards a robust audit framework for prospective safety analysis, empowering developers to audit and mitigate ASR disparities prior to deployment.

