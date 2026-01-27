---
layout: default
title: A Pragmatic VLA Foundation Model
---

# A Pragmatic VLA Foundation Model
**arXiv**：[2601.18692v1](https://arxiv.org/abs/2601.18692) · [PDF](https://arxiv.org/pdf/2601.18692.pdf)  
**作者**：Wei Wu, Fan Lu, Yunnan Wang, Shuai Yang, Shi Liu, Fangjing Wang, Qian Zhu, He Sun, Yong Wang, Shuailei Ma, Yiyu Ren, Kejia Zhang, Hui Yu, Jingmei Zhao, Shuai Zhou, Zhenqi Qiu, Houlong Xiong, Ziyu Wang, Zechen Wang, Ran Cheng, Yong-Lu Li, Yongtao Huang, Xing Zhu, Yujun Shen, Kecheng Zheng  

**一句话要点**：提出LingBot-VLA模型，基于真实世界数据实现机器人视觉-语言-动作任务的高效泛化与部署。

**关键词**：视觉-语言-动作模型, 机器人操作, 真实世界数据, 泛化能力, 高效训练, 开源基准

## 3 点简述
- 核心问题：开发成本高效且能跨任务和平台泛化的视觉-语言-动作基础模型，以支持机器人操作。
- 方法要点：使用约20,000小时来自9种双臂机器人的真实数据训练模型，并构建高效代码库提升训练速度。
- 实验或效果：在3个机器人平台上完成100个任务测试，模型表现优于竞争对手，展示强性能和广泛泛化能力。

## 摘要（原文）

> Offering great potential in robotic manipulation, a capable Vision-Language-Action (VLA) foundation model is expected to faithfully generalize across tasks and platforms while ensuring cost efficiency (e.g., data and GPU hours required for adaptation). To this end, we develop LingBot-VLA with around 20,000 hours of real-world data from 9 popular dual-arm robot configurations. Through a systematic assessment on 3 robotic platforms, each completing 100 tasks with 130 post-training episodes per task, our model achieves clear superiority over competitors, showcasing its strong performance and broad generalizability. We have also built an efficient codebase, which delivers a throughput of 261 samples per second per GPU with an 8-GPU training setup, representing a 1.5~2.8$\times$ (depending on the relied VLM base model) speedup over existing VLA-oriented codebases. The above features ensure that our model is well-suited for real-world deployment. To advance the field of robot learning, we provide open access to the code, base model, and benchmark data, with a focus on enabling more challenging tasks and promoting sound evaluation standards.

