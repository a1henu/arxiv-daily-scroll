---
layout: default
title: Learning State-Tracking from Code Using Linear RNNs
---

# Learning State-Tracking from Code Using Linear RNNs
**arXiv**：[2602.14814v1](https://arxiv.org/abs/2602.14814) · [PDF](https://arxiv.org/pdf/2602.14814.pdf)  
**作者**：Julien Siems, Riccardo Grazzi, Kirill Kalinin, Hitesh Ballani, Babak Rahmani  

**一句话要点**：提出通过代码转换解决状态跟踪任务与语言模型训练不兼容的问题，并比较线性RNN与Transformer的性能。

**关键词**：状态跟踪, 线性RNN, Transformer, 代码转换, 排列组合, 概率有限状态自动机

## 3 点简述
- 核心问题：状态跟踪任务（如排列组合）与语言模型的下一词预测训练设置不兼容。
- 方法要点：将排列组合转换为REPL跟踪代码，通过打印和变量变换揭示状态。
- 实验或效果：线性RNN在此设置下表现优异，而Transformer仍失败；但线性RNN在部分可观察状态跟踪中可能劣于非线性RNN。

## 摘要（原文）

> Over the last years, state-tracking tasks, particularly permutation composition, have become a testbed to understand the limits of sequence models architectures like Transformers and RNNs (linear and non-linear). However, these are often sequence-to-sequence tasks: learning to map actions (permutations) to states, which is incompatible with the next-token prediction setting commonly used to train language models. We address this gap by converting permutation composition into code via REPL traces that interleave state-reveals through prints and variable transformations. We show that linear RNNs capable of state-tracking excel also in this setting, while Transformers still fail. Motivated by this representation, we investigate why tracking states in code is generally difficult: actions are not always fully observable. We frame this as tracking the state of a probabilistic finite-state automaton with deterministic state reveals and show that linear RNNs can be worse than non-linear RNNs at tracking states in this setup.

