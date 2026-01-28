---
layout: default
title: When Benchmarks Leak: Inference-Time Decontamination for LLMs
---

# When Benchmarks Leak: Inference-Time Decontamination for LLMs
**arXiv**：[2601.19334v1](https://arxiv.org/abs/2601.19334) · [PDF](https://arxiv.org/pdf/2601.19334.pdf)  
**作者**：Jianzhe Chai, Yu Zhe, Jun Sakuma  

**一句话要点**：提出DeconIEP框架，在评估时通过输入嵌入扰动解决大语言模型测试集污染问题。

**关键词**：大语言模型评估, 测试集污染, 推理时去污, 嵌入扰动, 基准可靠性

## 3 点简述
- 核心问题：测试集污染导致大语言模型评估结果不可靠，现有方法或改变评估集或干扰正常推理。
- 方法要点：在评估时基于参考模型学习实例自适应扰动，引导模型远离记忆驱动的捷径路径。
- 实验或效果：在多个开源大语言模型和基准上，DeconIEP有效去污且对良性效用影响最小。

## 摘要（原文）

> Benchmark-based evaluation is the de facto standard for comparing large language models (LLMs). However, its reliability is increasingly threatened by test set contamination, where test samples or their close variants leak into training data and artificially inflate reported performance. To address this issue, prior work has explored two main lines of mitigation. One line attempts to identify and remove contaminated benchmark items before evaluation, but this inevitably alters the evaluation set itself and becomes unreliable when contamination is moderate or severe. The other line preserves the benchmark and instead suppresses contaminated behavior at evaluation time; however, such interventions often interfere with normal inference and lead to noticeable performance degradation on clean inputs. We propose DeconIEP, a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space. Guided by a relatively less-contaminated reference model, DeconIEP learns an instance-adaptive perturbation generator that steers the evaluated model away from memorization-driven shortcut pathways. Across multiple open-weight LLMs and benchmarks, extensive empirical results show that DeconIEP achieves strong decontamination effectiveness while incurring only minimal degradation in benign utility.

