---
layout: default
title: FlowAct-R1: Towards Interactive Humanoid Video Generation
---

# FlowAct-R1: Towards Interactive Humanoid Video Generation
**arXiv**：[2601.10103v1](https://arxiv.org/abs/2601.10103) · [PDF](https://arxiv.org/pdf/2601.10103.pdf)  
**作者**：Lizhen Wang, Yongming Zhu, Zhipeng Ge, Youwei Zheng, Longhao Zhang, Tianshu Hu, Shiyang Qin, Mingshuang Luo, Jiaxu Zhang, Xin Chen, Yulong Wang, Zerong Zheng, Jianwen Jiang, Chao Liang, Weifeng Chen, Xing Wang, Yuan Zhang, Mingyuan Gao  

**一句话要点**：提出FlowAct-R1框架以实现实时交互式人形视频生成，平衡高保真合成与低延迟需求。

**关键词**：交互式视频生成, 人形视频合成, 实时流式合成, 分块扩散强制, 时序一致性, 低延迟优化

## 3 点简述
- 核心问题：现有方法在高保真视频合成与实时交互需求间存在权衡，难以实现连续响应。
- 方法要点：基于MMDiT架构，采用分块扩散强制策略及自强制变体，确保长期时序一致性和低延迟流式合成。
- 实验或效果：在480p分辨率下实现稳定25fps，首帧延迟约1.5秒，展现高行为生动性和感知真实感，泛化性强。

## 摘要（原文）

> Interactive humanoid video generation aims to synthesize lifelike visual agents that can engage with humans through continuous and responsive video. Despite recent advances in video synthesis, existing methods often grapple with the trade-off between high-fidelity synthesis and real-time interaction requirements. In this paper, we propose FlowAct-R1, a framework specifically designed for real-time interactive humanoid video generation. Built upon a MMDiT architecture, FlowAct-R1 enables the streaming synthesis of video with arbitrary durations while maintaining low-latency responsiveness. We introduce a chunkwise diffusion forcing strategy, complemented by a novel self-forcing variant, to alleviate error accumulation and ensure long-term temporal consistency during continuous interaction. By leveraging efficient distillation and system-level optimizations, our framework achieves a stable 25fps at 480p resolution with a time-to-first-frame (TTFF) of only around 1.5 seconds. The proposed method provides holistic and fine-grained full-body control, enabling the agent to transition naturally between diverse behavioral states in interactive scenarios. Experimental results demonstrate that FlowAct-R1 achieves exceptional behavioral vividness and perceptual realism, while maintaining robust generalization across diverse character styles.

