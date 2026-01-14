---
layout: default
title: STAR: Detecting Inference-time Backdoors in LLM Reasoning via State-Transition Amplification Ratio
---

# STAR: Detecting Inference-time Backdoors in LLM Reasoning via State-Transition Amplification Ratio
**arXiv**：[2601.08511v1](https://arxiv.org/abs/2601.08511) · [PDF](https://arxiv.org/pdf/2601.08511.pdf)  
**作者**：Seong-Gyu Park, Sohee Park, Jisu Lee, Hyunsik Na, Daeseon Choi  

**一句话要点**：提出STAR框架，通过状态转移放大比检测LLM推理中的推理时后门攻击。

**关键词**：推理时后门检测, 状态转移放大比, CUSUM算法, LLM推理安全, 概率分布分析

## 3 点简述
- 核心问题：LLM推理机制如CoT易受推理时后门攻击，攻击注入恶意路径而不改参数，难以检测。
- 方法要点：利用恶意路径后验概率高但先验概率低的统计差异，量化状态转移放大，结合CUSUM算法检测异常。
- 实验或效果：在8B-70B模型和五个数据集上，STAR实现AUROC≈1.0，效率比基线高约42倍，且对自适应攻击鲁棒。

## 摘要（原文）

> Recent LLMs increasingly integrate reasoning mechanisms like Chain-of-Thought (CoT). However, this explicit reasoning exposes a new attack surface for inference-time backdoors, which inject malicious reasoning paths without altering model parameters. Because these attacks generate linguistically coherent paths, they effectively evade conventional detection. To address this, we propose STAR (State-Transition Amplification Ratio), a framework that detects backdoors by analyzing output probability shifts. STAR exploits the statistical discrepancy where a malicious input-induced path exhibits high posterior probability despite a low prior probability in the model's general knowledge. We quantify this state-transition amplification and employ the CUSUM algorithm to detect persistent anomalies. Experiments across diverse models (8B-70B) and five benchmark datasets demonstrate that STAR exhibits robust generalization capabilities, consistently achieving near-perfect performance (AUROC $\approx$ 1.0) with approximately $42\times$ greater efficiency than existing baselines. Furthermore, the framework proves robust against adaptive attacks attempting to bypass detection.

