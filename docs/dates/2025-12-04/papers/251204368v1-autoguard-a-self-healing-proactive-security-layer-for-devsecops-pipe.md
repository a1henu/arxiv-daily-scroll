---
layout: default
title: AutoGuard: A Self-Healing Proactive Security Layer for DevSecOps Pipelines Using Reinforcement Learning
---

# AutoGuard: A Self-Healing Proactive Security Layer for DevSecOps Pipelines Using Reinforcement Learning
**arXiv**：[2512.04368v1](https://arxiv.org/abs/2512.04368) · [PDF](https://arxiv.org/pdf/2512.04368.pdf)  
**作者**：Praveen Anugula, Avdhesh Kumar Bhardwaj, Navin Chhibber, Rohit Tewari, Sunil Khemka, Piyush Ranjan  

**一句话要点**：提出AutoGuard，一种基于强化学习的自愈安全框架，以主动保护DevSecOps管道。

**关键词**：DevSecOps安全, 强化学习应用, 自愈安全框架, CI/CD管道, 自动化威胁缓解

## 3 点简述
- 核心问题：现有基于规则的入侵检测和静态漏洞扫描方法响应慢，不适应系统变化，导致安全风险。
- 方法要点：使用强化学习代理动态学习策略，持续观察管道活动并主动修复异常，实现实时安全防护。
- 实验或效果：在模拟CI/CD环境中测试，威胁检测准确率提升22%，平均恢复时间减少38%，整体韧性增强。

## 摘要（原文）

> Contemporary DevSecOps pipelines have to deal with the evolution of security in an ever-continuously integrated and deployed environment. Existing methods,such as rule-based intrusion detection and static vulnerability scanning, are inadequate and unreceptive to changes in the system, causing longer response times and organization needs exposure to emerging attack vectors. In light of the previous constraints, we introduce AutoGuard to the DevSecOps ecosystem, a reinforcement learning (RL)-powered self-healing security framework built to pre-emptively protect DevSecOps environments. AutoGuard is a self-securing security environment that continuously observes pipeline activities for potential anomalies while preemptively remediating the environment. The model observes and reacts based on a policy that is continually learned dynamically over time. The RL agent improves each action over time through reward-based learning aimed at improving the agent's ability to prevent, detect and respond to a security incident in real-time. Testing using simulated ContinuousIntegration / Continuous Deployment (CI/CD) environments showed AutoGuard to successfully improve threat detection accuracy by 22%, reduce mean time torecovery (MTTR) for incidents by 38% and increase overall resilience to incidents as compared to traditional methods.
>   Keywords- DevSecOps, Reinforcement Learning, Self- Healing Security, Continuous Integration, Automated Threat Mitigation

