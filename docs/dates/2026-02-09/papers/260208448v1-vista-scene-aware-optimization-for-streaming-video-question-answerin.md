---
layout: default
title: Vista: Scene-Aware Optimization for Streaming Video Question Answering under Post-Hoc Queries
---

# Vista: Scene-Aware Optimization for Streaming Video Question Answering under Post-Hoc Queries
**arXiv**：[2602.08448v1](https://arxiv.org/abs/2602.08448) · [PDF](https://arxiv.org/pdf/2602.08448.pdf)  
**作者**：Haocheng Lu, Nan Zhang, Wei Tao, Xiaoyang Qu, Guokuan Li, Jiguang Wan, Jianzong Wang  

**一句话要点**：提出Vista框架以解决流式视频问答中的场景感知优化问题

**关键词**：流式视频问答, 场景感知优化, 多模态大语言模型, 长视频理解, 实时推理

## 3 点简述
- 核心问题：流式视频问答中视频帧顺序到达和查询任意时间点导致上下文丢失或内存溢出
- 方法要点：动态聚类帧为场景单元，压缩存储并选择性召回以提升效率和完整性
- 实验或效果：在StreamingBench上实现最先进性能，支持长上下文推理且不牺牲延迟或内存效率

## 摘要（原文）

> Streaming video question answering (Streaming Video QA) poses distinct challenges for multimodal large language models (MLLMs), as video frames arrive sequentially and user queries can be issued at arbitrary time points. Existing solutions relying on fixed-size memory or naive compression often suffer from context loss or memory overflow, limiting their effectiveness in long-form, real-time scenarios. We present Vista, a novel framework for scene-aware streaming video QA that enables efficient and scalable reasoning over continuous video streams. The innovation of Vista can be summarized in three aspects: (1) scene-aware segmentation, where Vista dynamically clusters incoming frames into temporally and visually coherent scene units; (2) scene-aware compression, where each scene is compressed into a compact token representation and stored in GPU memory for efficient index-based retrieval, while full-resolution frames are offloaded to CPU memory; and (3) scene-aware recall, where relevant scenes are selectively recalled and reintegrated into the model input upon receiving a query, enabling both efficiency and completeness. Vista is model-agnostic and integrates seamlessly with a variety of vision-language backbones, enabling long-context reasoning without compromising latency or memory efficiency. Extensive experiments on StreamingBench demonstrate that Vista achieves state-of-the-art performance, establishing a strong baseline for real-world streaming video understanding.

