---
layout: default
title: When and Where to Reset Matters for Long-Term Test-Time Adaptation
---

# When and Where to Reset Matters for Long-Term Test-Time Adaptation
**arXiv**：[2603.03796v1](https://arxiv.org/abs/2603.03796) · [PDF](https://arxiv.org/pdf/2603.03796.pdf)  
**作者**：Taejun Lim, Joong-Won Hwang, Kibok Lee  

**一句话要点**：提出自适应选择性重置方案，以解决长时测试时适应中的模型崩溃问题。

**关键词**：测试时适应, 模型崩溃, 自适应重置, 长时适应, 域偏移

## 3 点简述
- 核心问题：长时测试时适应中，错误累积导致模型崩溃，预测类别减少。
- 方法要点：动态决定重置时机与位置，结合重要性正则化恢复知识，增强适应性。
- 实验或效果：在长时测试时适应基准上验证有效性，尤其在挑战性域偏移下表现优异。

## 摘要（原文）

> When continual test-time adaptation (TTA) persists over the long term, errors accumulate in the model and further cause it to predict only a few classes for all inputs, a phenomenon known as model collapse. Recent studies have explored reset strategies that completely erase these accumulated errors. However, their periodic resets lead to suboptimal adaptation, as they occur independently of the actual risk of collapse. Moreover, their full resets cause catastrophic loss of knowledge acquired over time, even though such knowledge could be beneficial in the future. To this end, we propose (1) an Adaptive and Selective Reset (ASR) scheme that dynamically determines when and where to reset, (2) an importance-aware regularizer to recover essential knowledge lost due to reset, and (3) an on-the-fly adaptation adjustment scheme to enhance adaptability under challenging domain shifts. Extensive experiments across long-term TTA benchmarks demonstrate the effectiveness of our approach, particularly under challenging conditions. Our code is available at https://github.com/YonseiML/asr.

