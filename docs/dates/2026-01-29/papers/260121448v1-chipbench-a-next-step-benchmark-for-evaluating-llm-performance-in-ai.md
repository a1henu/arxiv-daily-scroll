---
layout: default
title: ChipBench: A Next-Step Benchmark for Evaluating LLM Performance in AI-Aided Chip Design
---

# ChipBench: A Next-Step Benchmark for Evaluating LLM Performance in AI-Aided Chip Design
**arXiv**：[2601.21448v1](https://arxiv.org/abs/2601.21448) · [PDF](https://arxiv.org/pdf/2601.21448.pdf)  
**作者**：Zhongkai Yu, Chenyang Zhou, Yichen Lin, Hejia Zhang, Haotian Ye, Junxia Cui, Zaifeng Pan, Jishen Zhao, Yufei Ding  

**一句话要点**：提出ChipBench基准以评估LLM在AI辅助芯片设计中的性能

**关键词**：AI辅助芯片设计, LLM基准评估, Verilog生成, 硬件调试, 参考模型生成

## 3 点简述
- 当前基准存在饱和和任务多样性不足问题，无法反映LLM在真实工业流程中的表现
- 基准包含Verilog生成、调试和参考模型生成三个关键任务，覆盖44个模块、89个调试案例和132个样本
- 评估显示SOTA模型性能显著低于饱和基准，如Claude-4.5-opus在Verilog生成中仅达30.74%

## 摘要（原文）

> While Large Language Models (LLMs) show significant potential in hardware engineering, current benchmarks suffer from saturation and limited task diversity, failing to reflect LLMs' performance in real industrial workflows. To address this gap, we propose a comprehensive benchmark for AI-aided chip design that rigorously evaluates LLMs across three critical tasks: Verilog generation, debugging, and reference model generation. Our benchmark features 44 realistic modules with complex hierarchical structures, 89 systematic debugging cases, and 132 reference model samples across Python, SystemC, and CXXRTL. Evaluation results reveal substantial performance gaps, with state-of-the-art Claude-4.5-opus achieving only 30.74\% on Verilog generation and 13.33\% on Python reference model generation, demonstrating significant challenges compared to existing saturated benchmarks where SOTA models achieve over 95\% pass rates. Additionally, to help enhance LLM reference model generation, we provide an automated toolbox for high-quality training data generation, facilitating future research in this underexplored domain. Our code is available at https://github.com/zhongkaiyu/ChipBench.git.

