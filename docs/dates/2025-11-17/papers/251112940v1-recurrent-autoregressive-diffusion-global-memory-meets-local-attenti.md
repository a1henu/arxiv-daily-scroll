---
layout: default
title: Recurrent Autoregressive Diffusion: Global Memory Meets Local Attention
---

# Recurrent Autoregressive Diffusion: Global Memory Meets Local Attention
**arXiv**：[2511.12940v1](https://arxiv.org/abs/2511.12940) · [PDF](https://arxiv.org/pdf/2511.12940.pdf)  
**作者**：Taiye Chen, Zihan Ding, Anjian Li, Christina Zhang, Zeqi Xiao, Yisen Wang, Chi Jin  

**一句话要点**：提出RAD框架结合LSTM与注意力，解决长视频生成中的记忆遗忘问题。

**关键词**：长视频生成, 扩散模型, 循环神经网络, 记忆压缩, 自回归生成

## 3 点简述
- 核心问题：现有视频扩散模型在长序列生成中因缺乏有效记忆压缩而遗忘历史信息。
- 方法要点：引入RNN和LSTM到扩散变换器，实现帧级自回归记忆更新与检索。
- 实验或效果：在Memory Maze和Minecraft数据集上验证RAD在长视频生成中的优越性。

## 摘要（原文）

> Recent advancements in video generation have demonstrated the potential of using video diffusion models as world models, with autoregressive generation of infinitely long videos through masked conditioning. However, such models, usually with local full attention, lack effective memory compression and retrieval for long-term generation beyond the window size, leading to issues of forgetting and spatiotemporal inconsistencies. To enhance the retention of historical information within a fixed memory budget, we introduce a recurrent neural network (RNN) into the diffusion transformer framework. Specifically, a diffusion model incorporating LSTM with attention achieves comparable performance to state-of-the-art RNN blocks, such as TTT and Mamba2. Moreover, existing diffusion-RNN approaches often suffer from performance degradation due to training-inference gap or the lack of overlap across windows. To address these limitations, we propose a novel Recurrent Autoregressive Diffusion (RAD) framework, which executes frame-wise autoregression for memory update and retrieval, consistently across training and inference time. Experiments on Memory Maze and Minecraft datasets demonstrate the superiority of RAD for long video generation, highlighting the efficiency of LSTM in sequence modeling.

