---
layout: default
title: Compact Prompting in Instruction-tuned LLMs for Joint Argumentative Component Detection
---

# Compact Prompting in Instruction-tuned LLMs for Joint Argumentative Component Detection
**arXiv**：[2603.03095v1](https://arxiv.org/abs/2603.03095) · [PDF](https://arxiv.org/pdf/2603.03095.pdf)  
**作者**：Sofiane Elguendouze, Erwan Hain, Elena Cabrio, Serena Villata  

**一句话要点**：提出基于指令调优大语言模型的紧凑提示方法，将论辩成分检测重构为生成任务。

**关键词**：论辩成分检测, 指令调优, 大语言模型, 生成任务, 紧凑提示, 论辩挖掘

## 3 点简述
- 核心问题：论辩成分检测需联合界定论辩跨度并分类为如主张和前提的组件，现有方法多简化为序列标注或流水线处理。
- 方法要点：使用指令调优大语言模型，通过紧凑指令提示将任务重构为语言生成，直接从文本识别论辩成分。
- 实验或效果：在标准基准测试中，该方法相比最先进系统实现了更高性能，突显指令调优在复杂论辩挖掘中的潜力。

## 摘要（原文）

> Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying them into components such as claims and premises. While research on this subtask remains relatively limited compared to other AM tasks, most existing approaches formulate it as a simplified sequence labeling problem, component classification, or a pipeline of component segmentation followed by classification. In this paper, we propose a novel approach based on instruction-tuned Large Language Models (LLMs) using compact instruction-based prompts, and reframe ACD as a language generation task, enabling arguments to be identified directly from plain text without relying on pre-segmented components. Experiments on standard benchmarks show that our approach achieves higher performance compared to state-of-the-art systems. To the best of our knowledge, this is one of the first attempts to fully model ACD as a generative task, highlighting the potential of instruction tuning for complex AM problems.

