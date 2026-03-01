---
layout: default
title: MSJoE: Jointly Evolving MLLM and Sampler for Efficient Long-Form Video Understanding
---

# MSJoE: Jointly Evolving MLLM and Sampler for Efficient Long-Form Video Understanding
**arXiv**：[2602.22932v1](https://arxiv.org/abs/2602.22932) · [PDF](https://arxiv.org/pdf/2602.22932.pdf)  
**作者**：Wenhui Tan, Xiaoyi Yu, Jiaze Li, Yijing Chen, Jianzhong Ju, Zhenbo Luo, Ruihua Song, Jian Luan  

**一句话要点**：提出MSJoE框架，联合进化MLLM与采样器以高效理解长视频。

**关键词**：长视频理解, 多模态大语言模型, 关键帧采样, 强化学习, 视频问答

## 3 点简述
- 核心问题：MLLM高效理解长视频面临挑战，需处理大量冗余帧。
- 方法要点：通过查询推理生成相似矩阵，轻量采样器选择关键帧，MLLM与采样器联合强化学习优化。
- 实验或效果：在多个数据集上实现8.0%准确率提升，优于基线方法1.1%。

## 摘要（原文）

> Efficiently understanding long-form videos remains a fundamental challenge for multimodal large language models (MLLMs). In this paper, we present MLLM-Sampler Joint Evolution (MSJoE), a novel framework that jointly evolves the MLLM and a lightweight key-frame sampler for efficient long-form video understanding. MSJoE builds upon a key assumption that only a small subset of key-frames is truly informative for answering each question to a video. Specifically, MSJoE first reasons out several queries, which describe diverse visual perspectives relevant to the question. Then, these queries interact with a frozen CLIP model to produce a query-frame similarity matrix. Finally, a lightweight sampler predicts key-frame sampling weights from this matrix, selecting a compact set of informative frames, which are then fed into the MLLM for answer generation. Both the MLLM and sampler are jointly optimized through reinforcement learning, enabling co-adaptation of query-reasoning, frame-sampling, and key-frame understanding. A new long-video QA dataset containing 2.8K videos with 7K question-answer pairs is collected to support the training process. Extensive experiments on VideoMME, LongVideoBench, LVBench, and MLVU show that MSJoE achieves 8.0\% accuracy gain upon the base MLLM, and 1.1\% higher accuracy than strongest baseline method.

