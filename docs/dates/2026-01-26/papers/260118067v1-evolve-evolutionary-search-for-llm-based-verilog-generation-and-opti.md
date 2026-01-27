---
layout: default
title: EvolVE: Evolutionary Search for LLM-based Verilog Generation and Optimization
---

# EvolVE: Evolutionary Search for LLM-based Verilog Generation and Optimization
**arXiv**：[2601.18067v1](https://arxiv.org/abs/2601.18067) · [PDF](https://arxiv.org/pdf/2601.18067.pdf)  
**作者**：Wei-Po Hsin, Ren-Hao Deng, Yao-Ting Hsieh, En-Ming Huang, Shih-Hao Hung  

**一句话要点**：提出EvolVE框架，结合进化搜索与LLM以自动化Verilog生成与优化

**关键词**：Verilog生成, 进化搜索, 硬件设计自动化, LLM优化, 蒙特卡洛树搜索, 结构化测试台生成

## 3 点简述
- 核心问题：Verilog设计依赖专家经验，LLM因数据有限和顺序推理难以处理硬件并发逻辑
- 方法要点：集成MCTS和IGR进化策略，利用STG加速搜索，提升功能正确性和优化效果
- 实验或效果：在VerilogEval v2和RTLLM v2达SOTA，IC-RTL基准上PPA产品最高降低66%

## 摘要（原文）

> Verilog's design cycle is inherently labor-intensive and necessitates extensive domain expertise. Although Large Language Models (LLMs) offer a promising pathway toward automation, their limited training data and intrinsic sequential reasoning fail to capture the strict formal logic and concurrency inherent in hardware systems. To overcome these barriers, we present EvolVE, the first framework to analyze multiple evolution strategies on chip design tasks, revealing that Monte Carlo Tree Search (MCTS) excels at maximizing functional correctness, while Idea-Guided Refinement (IGR) proves superior for optimization. We further leverage Structured Testbench Generation (STG) to accelerate the evolutionary process. To address the lack of complex optimization benchmarks, we introduce IC-RTL, targeting industry-scale problems derived from the National Integrated Circuit Contest. Evaluations establish EvolVE as the new state-of-the-art, achieving 98.1% on VerilogEval v2 and 92% on RTLLM v2. Furthermore, on the industry-scale IC-RTL suite, our framework surpasses reference implementations authored by contest participants, reducing the Power, Performance, Area (PPA) product by up to 66% in Huffman Coding and 17% in the geometric mean across all problems. The source code of the IC-RTL benchmark is available at https://github.com/weiber2002/ICRTL.

