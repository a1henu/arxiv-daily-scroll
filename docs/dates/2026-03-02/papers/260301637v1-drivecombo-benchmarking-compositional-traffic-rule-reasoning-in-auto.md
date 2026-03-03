---
layout: default
title: DriveCombo: Benchmarking Compositional Traffic Rule Reasoning in Autonomous Driving
---

# DriveCombo: Benchmarking Compositional Traffic Rule Reasoning in Autonomous Driving
**arXiv**：[2603.01637v1](https://arxiv.org/abs/2603.01637) · [PDF](https://arxiv.org/pdf/2603.01637.pdf)  
**作者**：Enhui Ma, Jiahuan Zhang, Guantian Zheng, Tao Tang, Shengbo Eben Li, Yuhang Lu, Xia Zhou, Xueyang Zhang, Yifei Zhan, Kun Zhan, Zhihui Hao, Xianpeng Lang, Kaicheng Yu  

**一句话要点**：提出DriveCombo基准以评估自动驾驶中多模态大语言模型的组合交通规则推理能力

**关键词**：自动驾驶基准, 组合推理, 交通规则理解, 多模态大语言模型, 认知阶梯评估

## 3 点简述
- 现有基准多关注单规则场景，忽略真实驾驶中多规则并发与冲突的复杂性。
- 提出五级认知阶梯和Rule2Scene代理，系统评估从单规则理解到多规则整合与冲突解决的推理能力。
- 评估14个主流MLLM显示性能随任务复杂度下降，微调后交通规则推理和下游规划能力显著提升。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) are rapidly becoming the intelligence brain of end-to-end autonomous driving systems. A key challenge is to assess whether MLLMs can truly understand and follow complex real-world traffic rules. However, existing benchmarks mainly focus on single-rule scenarios like traffic sign recognition, neglecting the complexity of multi-rule concurrency and conflicts in real driving. Consequently, models perform well on simple tasks but often fail or violate rules in real world complex situations. To bridge this gap, we propose DriveCombo, a text and vision-based benchmark for compositional traffic rule reasoning. Inspired by human drivers' cognitive development, we propose a systematic Five-Level Cognitive Ladder that evaluates reasoning from single-rule understanding to multi-rule integration and conflict resolution, enabling quantitative assessment across cognitive stages. We further propose a Rule2Scene Agent that maps language-based traffic rules to dynamic driving scenes through rule crafting and scene generation, enabling scene-level traffic rule visual reasoning. Evaluations of 14 mainstream MLLMs reveal performance drops as task complexity grows, particularly during rule conflicts. After splitting the dataset and fine-tuning on the training set, we further observe substantial improvements in both traffic rule reasoning and downstream planning capabilities. These results highlight the effectiveness of DriveCombo in advancing compliant and intelligent autonomous driving systems.

