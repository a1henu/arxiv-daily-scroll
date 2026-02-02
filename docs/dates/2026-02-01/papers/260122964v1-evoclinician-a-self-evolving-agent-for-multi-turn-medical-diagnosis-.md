---
layout: default
title: EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning
---

# EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning
**arXiv**：[2601.22964v1](https://arxiv.org/abs/2601.22964) · [PDF](https://arxiv.org/pdf/2601.22964.pdf)  
**作者**：Yufei He, Juncheng Liu, Zhiyuan Hu, Yulin Chen, Yue Liu, Yuan Sui, Yibo Li, Nuo Chen, Jun Hu, Bryan Hooi, Xinxing Xu, Jiang Bian  

**一句话要点**：提出EvoClinician自进化代理，通过测试时进化学习解决多轮医疗诊断问题

**关键词**：医疗诊断代理, 多轮诊断, 测试时进化学习, 临床基准, 自进化系统, 资源效率优化

## 3 点简述
- 核心问题：现有医疗AI基于一次性诊断，而真实诊断需多轮迭代询问以平衡信息获取与资源成本
- 方法要点：设计'诊断-评分-进化'循环，通过Actor代理诊断、Process Grader代理评估行动、Evolver代理更新策略
- 实验或效果：在Med-Inquire基准上优于持续学习基线和其他自进化代理，代码已开源

## 摘要（原文）

> Prevailing medical AI operates on an unrealistic ''one-shot'' model, diagnosing from a complete patient file. However, real-world diagnosis is an iterative inquiry where Clinicians sequentially ask questions and order tests to strategically gather information while managing cost and time. To address this, we first propose Med-Inquire, a new benchmark designed to evaluate an agent's ability to perform multi-turn diagnosis. Built upon a dataset of real-world clinical cases, Med-Inquire simulates the diagnostic process by hiding a complete patient file behind specialized Patient and Examination agents. They force the agent to proactively ask questions and order tests to gather information piece by piece. To tackle the challenges posed by Med-Inquire, we then introduce EvoClinician, a self-evolving agent that learns efficient diagnostic strategies at test time. Its core is a ''Diagnose-Grade-Evolve'' loop: an Actor agent attempts a diagnosis; a Process Grader agent performs credit assignment by evaluating each action for both clinical yield and resource efficiency; finally, an Evolver agent uses this feedback to update the Actor's strategy by evolving its prompt and memory. Our experiments show EvoClinician outperforms continual learning baselines and other self-evolving agents like memory agents. The code is available at https://github.com/yf-he/EvoClinician

