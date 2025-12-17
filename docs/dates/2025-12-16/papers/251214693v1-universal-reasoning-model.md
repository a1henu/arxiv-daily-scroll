---
layout: default
title: Universal Reasoning Model
---

# Universal Reasoning Model
**arXiv**：[2512.14693v1](https://arxiv.org/abs/2512.14693) · [PDF](https://arxiv.org/pdf/2512.14693.pdf)  
**作者**：Zitian Gao, Lynx Chen, Yihao Xiao, He Xing, Ran Tao, Haoming Luo, Joey Zhou, Bryan Dai  

**一句话要点**：提出通用推理模型以提升复杂推理任务性能，如ARC-AGI和数独。

**关键词**：通用推理模型, Transformer分析, 复杂推理任务, ARC-AGI, 短卷积, 截断反向传播

## 3 点简述
- 分析通用Transformer变体，发现性能提升源于循环归纳偏置和强非线性组件。
- 提出URM，通过短卷积和截断反向传播增强通用Transformer。
- 在ARC-AGI上实现最先进性能，如53.8% pass@1。

## 摘要（原文）

> Universal transformers (UTs) have been widely used for complex reasoning tasks such as ARC-AGI and Sudoku, yet the specific sources of their performance gains remain underexplored. In this work, we systematically analyze UTs variants and show that improvements on ARC-AGI primarily arise from the recurrent inductive bias and strong nonlinear components of Transformer, rather than from elaborate architectural designs. Motivated by this finding, we propose the Universal Reasoning Model (URM), which enhances the UT with short convolution and truncated backpropagation. Our approach substantially improves reasoning performance, achieving state-of-the-art 53.8% pass@1 on ARC-AGI 1 and 16.0% pass@1 on ARC-AGI 2. Our code is avaliable at https://github.com/zitian-gao/URM.

