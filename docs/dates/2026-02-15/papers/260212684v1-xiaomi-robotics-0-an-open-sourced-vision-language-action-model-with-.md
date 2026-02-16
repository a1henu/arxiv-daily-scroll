---
layout: default
title: Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution
---

# Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution
**arXiv**：[2602.12684v1](https://arxiv.org/abs/2602.12684) · [PDF](https://arxiv.org/pdf/2602.12684.pdf)  
**作者**：Rui Cai, Jun Guo, Xinze He, Piaopiao Jin, Jie Li, Bingxuan Lin, Futeng Liu, Wei Liu, Fei Ma, Kun Ma, Feng Qiu, Heng Qu, Yifei Su, Qiao Sun, Dong Wang, Donghao Wang, Yunhong Wang, Rujie Wu, Diyun Xiang, Yu Yang, Hangjun Ye, Yuan Zhang, Quanyun Zhou  

**一句话要点**：提出Xiaomi-Robotics-0视觉-语言-动作模型，通过异步执行训练与部署策略实现实时机器人操作

**关键词**：视觉-语言-动作模型, 实时机器人执行, 异步训练, 跨体现预训练, 双手操作, 开源模型

## 3 点简述
- 核心问题：视觉-语言-动作模型在实时机器人部署中面临推理延迟与动作连续性挑战
- 方法要点：结合大规模跨体现轨迹预训练与异步执行后训练，优化模型性能与实时执行
- 实验或效果：在仿真基准和真实机器人双手操作任务中达到先进性能，支持消费级GPU流畅运行

## 摘要（原文）

> In this report, we introduce Xiaomi-Robotics-0, an advanced vision-language-action (VLA) model optimized for high performance and fast and smooth real-time execution. The key to our method lies in a carefully designed training recipe and deployment strategy. Xiaomi-Robotics-0 is first pre-trained on large-scale cross-embodiment robot trajectories and vision-language data, endowing it with broad and generalizable action-generation capabilities while avoiding catastrophic forgetting of the visual-semantic knowledge of the underlying pre-trained VLM. During post-training, we propose several techniques for training the VLA model for asynchronous execution to address the inference latency during real-robot rollouts. During deployment, we carefully align the timesteps of consecutive predicted action chunks to ensure continuous and seamless real-time rollouts. We evaluate Xiaomi-Robotics-0 extensively in simulation benchmarks and on two challenging real-robot tasks that require precise and dexterous bimanual manipulation. Results show that our method achieves state-of-the-art performance across all simulation benchmarks. Moreover, Xiaomi-Robotics-0 can roll out fast and smoothly on real robots using a consumer-grade GPU, achieving high success rates and throughput on both real-robot tasks. To facilitate future research, code and model checkpoints are open-sourced at https://xiaomi-robotics-0.github.io

