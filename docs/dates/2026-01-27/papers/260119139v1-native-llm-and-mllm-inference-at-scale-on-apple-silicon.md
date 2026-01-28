---
layout: default
title: Native LLM and MLLM Inference at Scale on Apple Silicon
---

# Native LLM and MLLM Inference at Scale on Apple Silicon
**arXiv**：[2601.19139v1](https://arxiv.org/abs/2601.19139) · [PDF](https://arxiv.org/pdf/2601.19139.pdf)  
**作者**：Wayner Barrios  

**一句话要点**：提出vllm-mlx框架以在Apple Silicon上高效运行LLM和MLLM推理

**关键词**：Apple Silicon推理, 多模态模型优化, 前缀缓存, 连续批处理, MLX框架, 硬件加速

## 3 点简述
- 核心问题：现有工具在Apple Silicon上缺乏原生优化或仅支持文本模型，多模态推理效率低
- 方法要点：基于MLX原生构建，文本模型采用连续批处理，多模态模型引入基于内容的图像前缀缓存
- 实验或效果：在M4 Max上，文本模型吞吐量最高提升87%，多模态查询加速28倍，视频分析缓存加速24.7倍

## 摘要（原文）

> The growing adoption of Apple Silicon for machine learning development has created demand for efficient inference solutions that leverage its unique unified memory architecture. However, existing tools either lack native optimization (PyTorch MPS) or focus solely on text models (llama.cpp), leaving multimodal workloads underserved. We present vllm-mlx, a framework for efficient LLM and MLLM inference on Apple Silicon built natively on MLX. For text models, we achieve 21% to 87% higher throughput than llama.cpp across models ranging from Qwen3-0.6B to Nemotron-30B, while providing continuous batching that scales to 4.3x aggregate throughput at 16 concurrent requests. For multimodal models, we introduce content-based prefix caching that eliminates redundant vision encoding by identifying identical images through content hashing, regardless of input format. Our evaluation on Apple M4 Max demonstrates throughput of up to 525 tokens per second on text models and 28x speedup on repeated image queries, reducing multimodal latency from 21.7 seconds to under 1 second. Video analysis with up to 64 frames achieves 24.7x cache speedup. We release our implementation as open source to support efficient inference on consumer Apple hardware.

