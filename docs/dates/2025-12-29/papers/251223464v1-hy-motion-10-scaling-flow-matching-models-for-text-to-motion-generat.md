---
layout: default
title: HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation
---

# HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation
**arXiv**：[2512.23464v1](https://arxiv.org/abs/2512.23464) · [PDF](https://arxiv.org/pdf/2512.23464.pdf)  
**作者**：Yuxin Wen, Qing Shuai, Di Kang, Jing Li, Cheng Wen, Yue Qian, Ningxin Jiao, Changhai Chen, Weijie Chen, Yiran Wang, Jinkun Guo, Dongyue An, Han Liu, Yanyu Tong, Chao Zhang, Qing Guo, Juan Chen, Qiao Zhang, Youyi Zhang, Zihao Yao, Cheng Zhang, Hong Duan, Xiaoping Wu, Qi Chen, Fei Cheng, Liang Dong, Peng He, Hao Zhang, Jiaxin Lin, Chao Zhang, Zhongyi Fan, Yifan Li, Zhichao Hu, Yuhong Liu, Linus, Jie Jiang, Xiaolong Li, Linchao Bao  

**一句话要点**：提出HY-Motion 1.0，基于扩散Transformer的流匹配模型，用于文本到3D人体运动生成，实现十亿参数规模扩展。

**关键词**：文本到运动生成, 扩散Transformer, 流匹配模型, 大规模预训练, 强化学习, 3D人体运动

## 3 点简述
- 核心问题：文本到3D人体运动生成中，现有模型在参数规模和指令跟随能力上存在局限，需提升运动质量和文本对齐精度。
- 方法要点：采用全阶段训练范式，包括大规模预训练、高质量微调和基于人类反馈的强化学习，结合严格数据处理流程。
- 实验或效果：模型覆盖超过200个运动类别，在指令跟随能力上显著超越当前开源基准，支持开源以促进研究和商业化。

## 摘要（原文）

> We present HY-Motion 1.0, a series of state-of-the-art, large-scale, motion generation models capable of generating 3D human motions from textual descriptions. HY-Motion 1.0 represents the first successful attempt to scale up Diffusion Transformer (DiT)-based flow matching models to the billion-parameter scale within the motion generation domain, delivering instruction-following capabilities that significantly outperform current open-source benchmarks. Uniquely, we introduce a comprehensive, full-stage training paradigm -- including large-scale pretraining on over 3,000 hours of motion data, high-quality fine-tuning on 400 hours of curated data, and reinforcement learning from both human feedback and reward models -- to ensure precise alignment with the text instruction and high motion quality. This framework is supported by our meticulous data processing pipeline, which performs rigorous motion cleaning and captioning. Consequently, our model achieves the most extensive coverage, spanning over 200 motion categories across 6 major classes. We release HY-Motion 1.0 to the open-source community to foster future research and accelerate the transition of 3D human motion generation models towards commercial maturity.

