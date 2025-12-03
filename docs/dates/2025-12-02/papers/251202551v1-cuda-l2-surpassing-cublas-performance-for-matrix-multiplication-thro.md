---
layout: default
title: CUDA-L2: Surpassing cuBLAS Performance for Matrix Multiplication through Reinforcement Learning
---

# CUDA-L2: Surpassing cuBLAS Performance for Matrix Multiplication through Reinforcement Learning
**arXiv**：[2512.02551v1](https://arxiv.org/abs/2512.02551) · [PDF](https://arxiv.org/pdf/2512.02551.pdf)  
**作者**：Songqiao Su, Xiaofei Sun, Xiaoya Li, Albert Wang, Jiwei Li, Chris Shum  

**一句话要点**：提出CUDA-L2系统，结合大语言模型与强化学习自动优化半精度矩阵乘法CUDA内核，超越主流库性能。

**关键词**：矩阵乘法优化, 强化学习, 大语言模型, CUDA内核, 半精度计算, 自动化调优

## 3 点简述
- 核心问题：自动优化半精度矩阵乘法（HGEMM）CUDA内核以提升性能。
- 方法要点：使用大语言模型和强化学习，以CUDA执行速度为奖励，自动探索配置空间。
- 实验效果：在离线与服务器模式下，平均性能超越torch.matmul、cuBLAS和cuBLASLt等基准。

## 摘要（原文）

> In this paper, we propose CUDA-L2, a system that combines large language models (LLMs) and reinforcement learning (RL) to automatically optimize Half-precision General Matrix Multiply (HGEMM) CUDA kernels. Using CUDA execution speed as the RL reward, CUDA-L2 automatically optimizes HGEMM kernels across 1,000 configurations. CUDA-L2 systematically outperforms major matmul baselines to date, from the widely-used {\it torch.matmul} to state-of-the-art Nvidia's closed-source libraries, i.e., {\it cuBLAS}, {\it cuBLASLt}. In offline mode, where kernels are executed consecutively without time intervals, CUDA-L2 yields +22.0\% over {\it torch.matmul} on average; +19.2\% over {\it cuBLAS} using the optimal layout configuration (normal-normal NN and transposed-normal TN); +16.8\% over {\it cuBLASLt-heuristic}, which queries {\it cuBLASLt} library and selects the algorithm based on the heuristic's suggestion; and +11.4\% over the most competitive {\it cuBLASLt-AutoTuning} model, which selects the fastest algorithm from up to 100 candidates from {\it cuBLASLt}'s suggestions. In server mode, where kernels are executed at random intervals simulating real-time inference, the speedups further increase to +28.7\%, +26.0\%, +22.4\%, and +15.9\% for {\it torch.matmul}, {\it cuBLAS}, {\it cuBLASLt-heuristic}, and {\it cuBLASLt-AutoTuning} respectively. CUDA-L2 shows that even the most performance-critical, heavily-optimized kernels like HGEMM can be improved through LLM-guided RL automation by systematically exploring configuration spaces at scales impractical for humans. Project and code can be found at github.com/deepreinforce-ai/CUDA-L2

