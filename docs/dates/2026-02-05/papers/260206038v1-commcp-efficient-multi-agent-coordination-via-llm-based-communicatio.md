---
layout: default
title: CommCP: Efficient Multi-Agent Coordination via LLM-Based Communication with Conformal Prediction
---

# CommCP: Efficient Multi-Agent Coordination via LLM-Based Communication with Conformal Prediction
**arXiv**：[2602.06038v1](https://arxiv.org/abs/2602.06038) · [PDF](https://arxiv.org/pdf/2602.06038.pdf)  
**作者**：Xiaopan Zhang, Zejin Wang, Zhixu Li, Jianpeng Yao, Jiachen Li  

**一句话要点**：提出CommCP框架，基于LLM与保形预测提升多机器人协作中的通信效率与可靠性。

**关键词**：多智能体协作, 保形预测, 大语言模型, 具身问答, 机器人通信, 去中心化框架

## 3 点简述
- 核心问题：多机器人协作中信息收集效率低，通信冗余影响任务成功率。
- 方法要点：采用LLM生成消息，结合保形预测校准以减少接收方干扰。
- 实验或效果：在MM-EQA基准上显著提升任务成功率和探索效率。

## 摘要（原文）

> To complete assignments provided by humans in natural language, robots must interpret commands, generate and answer relevant questions for scene understanding, and manipulate target objects. Real-world deployments often require multiple heterogeneous robots with different manipulation capabilities to handle different assignments cooperatively. Beyond the need for specialized manipulation skills, effective information gathering is important in completing these assignments. To address this component of the problem, we formalize the information-gathering process in a fully cooperative setting as an underexplored multi-agent multi-task Embodied Question Answering (MM-EQA) problem, which is a novel extension of canonical Embodied Question Answering (EQA), where effective communication is crucial for coordinating efforts without redundancy. To address this problem, we propose CommCP, a novel LLM-based decentralized communication framework designed for MM-EQA. Our framework employs conformal prediction to calibrate the generated messages, thereby minimizing receiver distractions and enhancing communication reliability. To evaluate our framework, we introduce an MM-EQA benchmark featuring diverse, photo-realistic household scenarios with embodied questions. Experimental results demonstrate that CommCP significantly enhances the task success rate and exploration efficiency over baselines. The experiment videos, code, and dataset are available on our project website: https://comm-cp.github.io.

