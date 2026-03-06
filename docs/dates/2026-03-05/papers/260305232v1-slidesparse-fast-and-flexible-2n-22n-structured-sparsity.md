---
layout: default
title: SlideSparse: Fast and Flexible (2N-2):2N Structured Sparsity
---

# SlideSparse: Fast and Flexible (2N-2):2N Structured Sparsity
**arXiv**：[2603.05232v1](https://arxiv.org/abs/2603.05232) · [PDF](https://arxiv.org/pdf/2603.05232.pdf)  
**作者**：Hanyong Shao, Yingbo Hao, Ting Song, Yan Xia, Di Zhang, Shaohan Huang, Xun Wu, Songchen Xu, Le Xu, Li Dong, Zewen Chi, Yi Zou, Furu Wei  

**一句话要点**：提出SlideSparse系统，在通用GPU上实现(2N-2):2N结构化稀疏加速，以平衡LLM推理准确性与效率。

**关键词**：结构化稀疏, LLM推理加速, GPU优化, 滑动窗口分解, 激活提升, 稀疏张量核心

## 3 点简述
- 核心问题：NVIDIA 2:4稀疏张量核心要求50%剪枝，导致LLM推理准确性大幅下降，而更温和的(2N-2):2N模式无硬件支持。
- 方法要点：通过滑动窗口分解将(2N-2):2N权重块重构为N-1个重叠的2:4兼容窗口，结合激活提升技术融合激活重排。
- 实验或效果：在Qwen2.5-7B等模型上，6:8稀疏度下实测加速比达1.33倍，接近理论上限，保持准确性。

## 摘要（原文）

> NVIDIA's 2:4 Sparse Tensor Cores deliver 2x throughput but demand strict 50% pruning -- a ratio that collapses LLM reasoning accuracy (Qwen3: 54% to 15%). Milder $(2N-2):2N$ patterns (e.g., 6:8, 25% pruning) preserve accuracy yet receive no hardware support, falling back to dense execution without any benefit from sparsity. We present SlideSparse, the first system to unlock Sparse Tensor Core acceleration for the $(2N-2):2N$ model family on commodity GPUs. Our Sliding Window Decomposition reconstructs any $(2N-2):2N$ weight block into $N-1$ overlapping 2:4-compliant windows without any accuracy loss; Activation Lifting fuses the corresponding activation rearrangement into per-token quantization at near-zero cost. Integrated into vLLM, SlideSparse is evaluated across various GPUs (A100, H100, B200, RTX 4090, RTX 5080, DGX-spark), precisions (FP4, INT8, FP8, BF16, FP16), and model families (Llama, Qwen, BitNet). On compute-bound workloads, the measured speedup ratio (1.33x) approaches the theoretical upper-bound $N/(N-1)=4/3$ at 6:8 weight sparsity in Qwen2.5-7B, establishing $(2N-2):2N$ as a practical path to accuracy-preserving LLM acceleration. Code available at https://github.com/bcacdwk/vllmbench.

