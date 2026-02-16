---
layout: default
title: To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models
---

# To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models
**arXiv**：[2602.12566v1](https://arxiv.org/abs/2602.12566) · [PDF](https://arxiv.org/pdf/2602.12566.pdf)  
**作者**：Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang  

**一句话要点**：比较混合与合并训练范式，分析多领域强化学习在大语言模型中的协同效应

**关键词**：多领域强化学习, 大语言模型, 模型合并, 推理能力, 协同效应

## 3 点简述
- 核心问题：多领域RLVR训练范式（混合多任务与分离后合并）缺乏详细比较分析
- 方法要点：选择数学、编码等任务，通过几何、预测行为和信息约束分析内部机制
- 实验或效果：发现跨领域RLVR干扰少，推理密集型领域有协同增益

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) plays a key role in stimulating the explicit reasoning capability of Large Language Models (LLMs). We can achieve expert-level performance in some specific domains via RLVR, such as coding or math. When a general multi-domain expert-level model is required, we need to carefully consider the collaboration of RLVR across different domains. The current state-of-the-art models mainly employ two different training paradigms for multi-domain RLVR: mixed multi-task RLVR and separate RLVR followed by model merging. However, most of the works did not provide a detailed comparison and analysis about these paradigms. To this end, we choose multiple commonly used high-level tasks (e.g., math, coding, science, and instruction following) as our target domains and design extensive qualitative and quantitative experiments using open-source datasets. We find the RLVR across domains exhibits few mutual interferences, and reasoning-intensive domains demonstrate mutually synergistic effects. Furthermore, we analyze the internal mechanisms of mutual gains from the perspectives of weight space geometry, model prediction behavior, and information constraints. This project is named as M2RL that means Mixed multi-task training or separate training followed by model Merging for Reinforcement Learning, and the homepage is at https://github.com/mosAI25/M2RL

