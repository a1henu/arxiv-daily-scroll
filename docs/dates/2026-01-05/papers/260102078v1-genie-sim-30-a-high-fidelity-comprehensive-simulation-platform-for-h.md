---
layout: default
title: Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot
---

# Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot
**arXiv**：[2601.02078v1](https://arxiv.org/abs/2601.02078) · [PDF](https://arxiv.org/pdf/2601.02078.pdf)  
**作者**：Chenghao Yin, Da Huang, Di Yang, Jichao Wang, Nanshu Zhao, Chen Xu, Wenjun Sun, Linjie Hou, Zhijun Li, Junhui Wu, Zhaobo Liu, Zhen Xiao, Sheng Zhang, Lei Bao, Rui Feng, Zhenquan Pang, Jiayu Li, Qian Wang, Maoqing Yao  

**一句话要点**：提出Genie Sim 3.0仿真平台，以解决人形机器人训练数据不足和仿真到现实迁移的挑战。

**关键词**：人形机器人仿真, 大语言模型场景生成, 仿真到现实迁移, 自动化评估基准, 合成数据集

## 3 点简述
- 核心问题：机器人学习缺乏大规模、高保真仿真数据，现有仿真平台碎片化且保真度不足。
- 方法要点：利用大语言模型构建高保真场景，并引入基于LLM和VLM的自动化评估基准。
- 实验或效果：发布开源数据集，验证了合成数据在可控条件下可有效替代真实数据进行策略训练。

## 摘要（原文）

> The development of robust and generalizable robot learning models is critically contingent upon the availability of large-scale, diverse training data and reliable evaluation benchmarks. Collecting data in the physical world poses prohibitive costs and scalability challenges, and prevailing simulation benchmarks frequently suffer from fragmentation, narrow scope, or insufficient fidelity to enable effective sim-to-real transfer. To address these challenges, we introduce Genie Sim 3.0, a unified simulation platform for robotic manipulation. We present Genie Sim Generator, a large language model (LLM)-powered tool that constructs high-fidelity scenes from natural language instructions. Its principal strength resides in rapid and multi-dimensional generalization, facilitating the synthesis of diverse environments to support scalable data collection and robust policy evaluation. We introduce the first benchmark that pioneers the application of LLM for automated evaluation. It leverages LLM to mass-generate evaluation scenarios and employs Vision-Language Model (VLM) to establish an automated assessment pipeline. We also release an open-source dataset comprising more than 10,000 hours of synthetic data across over 200 tasks. Through systematic experimentation, we validate the robust zero-shot sim-to-real transfer capability of our open-source dataset, demonstrating that synthetic data can server as an effective substitute for real-world data under controlled conditions for scalable policy training. For code and dataset details, please refer to: https://github.com/AgibotTech/genie_sim.

