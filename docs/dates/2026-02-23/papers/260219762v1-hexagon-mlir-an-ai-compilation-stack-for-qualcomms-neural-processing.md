---
layout: default
title: Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)
---

# Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)
**arXiv**：[2602.19762v1](https://arxiv.org/abs/2602.19762) · [PDF](https://arxiv.org/pdf/2602.19762.pdf)  
**作者**：Mohammed Javed Absar, Muthu Baskaran, Abhikrant Sharma, Abhilash Bhandari, Ankit Aggarwal, Arun Rangasamy, Dibyendu Das, Fateme Hosseini, Franck Slama, Iulian Brumar, Jyotsna Verma, Krishnaprasad Bindumadhavan, Mitesh Kothari, Mohit Gupta, Ravishankar Kolachana, Richard Lethin, Samarth Narang, Sanjay Motilal Ladwa, Shalini Jain, Snigdha Suresh Dalvi, Tasmia Rahman, Venkat Rasagna Reddy Komatireddy, Vivek Vasudevbhai Pandya, Xiyue Shi, Zachary Zipper  

**一句话要点**：提出Hexagon-MLIR开源编译栈，以加速高通Hexagon NPU上的AI工作负载部署。

**关键词**：AI编译栈, 高通Hexagon NPU, MLIR框架, Triton内核, PyTorch模型, 数据局部性优化

## 3 点简述
- 核心问题：基于库的方法存在带宽瓶颈，影响AI模型在NPU上的性能。
- 方法要点：利用MLIR框架，通过结构化编译流程生成mega-kernels，优化数据局部性。
- 实验或效果：支持Triton内核和PyTorch模型，提供从内核到二进制的自动化编译，加速部署。

## 摘要（原文）

> In this paper, we present Hexagon-MLIR,an open-source compilation stack that targets Qualcomm Hexagon Neural Processing Unit (NPU) and provides unified support for lowering Triton kernels and PyTorch models . Built using the MLIR framework, our compiler applies a structured sequence of passes to exploit NPU architectural features to accelerate AI workloads. It enables faster deployment of new Triton kernels (hand-written or subgraphs from PyTorch 2.0), for our target by providing automated compilation from kernel to binary. By ingesting Triton kernels, we generate mega-kernels that maximize data locality in the NPU's Tightly Coupled Memory (TCM), reducing the bandwidth bottlenecks inherent in library-based approaches. This initiative complements our commercial toolchains by providing developers with an open-source MLIR-based compilation stack that gives them a path to advance AI compilation capabilities through a more flexible approach. Hexagon-MLIR is a work-in-progress, and we are continuing to add many more optimizations and capabilities in this effort.

