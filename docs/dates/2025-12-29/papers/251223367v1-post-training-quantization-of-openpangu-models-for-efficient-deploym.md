---
layout: default
title: Post-Training Quantization of OpenPangu Models for Efficient Deployment on Atlas A2
---

# Post-Training Quantization of OpenPangu Models for Efficient Deployment on Atlas A2
**arXiv**：[2512.23367v1](https://arxiv.org/abs/2512.23367) · [PDF](https://arxiv.org/pdf/2512.23367.pdf)  
**作者**：Yilun Luo, HuaQing Zheng, Haoqian Meng, Wenyuan Liu, Peng Zhang  

**一句话要点**：提出低比特量化框架以优化openPangu模型在Atlas A2上的部署效率

**关键词**：低比特量化, 推理优化, Ascend NPU部署, Chain-of-Thought推理, 模型压缩

## 3 点简述
- 针对openPangu-Embedded模型在Ascend NPU上推理时因CoT模式导致的内存和延迟问题
- 采用INT8和W4A8量化方法，将FP16计算转换为整数运算以提升效率
- 实验显示INT8量化保持90%以上精度并实现1.5倍预填充加速，W4A8量化显著降低内存消耗

## 摘要（原文）

> Huawei's openPangu-Embedded-1B and openPangu-Embedded-7B, variants of the openPangu large language model, integrate three distinct Chain-of-Thought (CoT) reasoning paradigms, namely slow_think, auto_think, and no_think. While these CoT modes enhance reasoning capabilities, their generation of extended reasoning traces introduces substantial memory and latency overheads, posing challenges for practical deployment on Ascend NPUs. This paper addresses these computational constraints by leveraging low-bit quantization, which transforms FP16 computations into more efficient integer arithmetic. We introduce a unified low-bit inference framework, supporting INT8 (W8A8) and W4A8 quantization, specifically optimized for openPangu-Embedded models on the Atlas A2. Our comprehensive evaluation, conducted across all three CoT modes on code generation benchmarks (HumanEval and MBPP), demonstrates the efficacy of this approach. INT8 quantization consistently preserves over 90\% of the FP16 baseline accuracy and achieves a 1.5x prefill speedup on the Atlas A2. Furthermore, W4A8 quantization significantly reduces memory consumption, albeit with a moderate trade-off in accuracy. These findings collectively indicate that low-bit quantization effectively facilitates efficient CoT reasoning on Ascend NPUs, maintaining high model fidelity.

