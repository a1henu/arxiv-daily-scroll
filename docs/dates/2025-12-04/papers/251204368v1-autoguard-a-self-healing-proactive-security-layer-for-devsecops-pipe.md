---
layout: default
title: AutoGuard: A Self-Healing Proactive Security Layer for DevSecOps Pipelines Using Reinforcement Learning
---

# AutoGuard: A Self-Healing Proactive Security Layer for DevSecOps Pipelines Using Reinforcement Learning
**arXiv**：[2512.04368v1](https://arxiv.org/abs/2512.04368) · [PDF](https://arxiv.org/pdf/2512.04368.pdf)  
**作者**：Praveen Anugula, Avdhesh Kumar Bhardwaj, Navin Chhibber, Rohit Tewari, Sunil Khemka, Piyush Ranjan  

**一句话要点**：提出AutoGuard，一种基于强化学习的自愈安全框架，以主动保护DevSecOps管道。

**关键词**：DevSecOps安全, 强化学习应用, 自愈安全框架, 自动化威胁缓解, CI/CD管道保护

## 3 点简述
- 核心问题：现有DevSecOps安全方法如规则检测和静态扫描响应慢，不适应系统变化，导致暴露于新攻击向量。
- 方法要点：使用强化学习代理动态学习策略，持续观察管道活动并主动修复异常，实现实时预防、检测和响应。
- 实验或效果：在模拟CI/CD环境中测试，威胁检测准确率提升22%，平均恢复时间减少38%，整体韧性增强。

## 摘要（原文）

> Contemporary DevSecOps pipelines have to deal with the evolution of security in an ever-continuously integrated and deployed environment. Existing methods,such as rule-based intrusion detection and static vulnerability scanning, are inadequate and unreceptive to changes in the system, causing longer response times and organization needs exposure to emerging attack vectors. In light of the previous constraints, we introduce AutoGuard to the DevSecOps ecosystem, a reinforcement learning (RL)-powered self-healing security framework built to pre-emptively protect DevSecOps environments. AutoGuard is a self-securing security environment that continuously observes pipeline activities for potential anomalies while preemptively remediating the environment. The model observes and reacts based on a policy that is continually learned dynamically over time. The RL agent improves each action over time through reward-based learning aimed at improving the agent's ability to prevent, detect and respond to a security incident in real-time. Testing using simulated ContinuousIntegration / Continuous Deployment (CI/CD) environments showed AutoGuard to successfully improve threat detection accuracy by 22%, reduce mean time torecovery (MTTR) for incidents by 38% and increase overall resilience to incidents as compared to traditional methods.
>   Keywords- DevSecOps, Reinforcement Learning, Self- Healing Security, Continuous Integration, Automated Threat Mitigation

