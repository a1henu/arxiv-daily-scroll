---
layout: default
title: Bohrium + SciMaster: Building the Infrastructure and Ecosystem for Agentic Science at Scale
---

# Bohrium + SciMaster: Building the Infrastructure and Ecosystem for Agentic Science at Scale
**arXiv**：[2512.20469v1](https://arxiv.org/abs/2512.20469) · [PDF](https://arxiv.org/pdf/2512.20469.pdf)  
**作者**：Linfeng Zhang, Siheng Chen, Yuzhu Cai, Jingyi Chai, Junhan Chang, Kun Chen, Zhi X. Chen, Zhaohan Ding, Yuwen Du, Yuanpeng Gao, Yuan Gao, Jing Gao, Zhifeng Gao, Qiangqiang Gu, Yanhui Hong, Yuan Huang, Xi Fang, Xiaohong Ji, Guolin Ke, Zixing Lei, Xinyu Li, Yongge Li, Ruoxue Liao, Hang Lin, Xiaolu Lin, Yuxiang Liu, Xinzijian Liu, Zexi Liu, Jintan Lu, Tingjia Miao, Haohui Que, Weijie Sun, Yanfeng Wang, Bingyang Wu, Tianju Xue, Rui Ye, Jinzhe Zeng, Duo Zhang, Jiahui Zhang, Linfeng Zhang, Tianhan Zhang, Wenchang Zhang, Yuzhi Zhang, Zezhong Zhang, Hang Zheng, Hui Zhou, Tong Zhu, Xinyu Zhu, Qingguo Zhou, Weinan E  

**一句话要点**：提出Bohrium+SciMaster基础设施与生态系统，以支持大规模代理化科学工作流。

**关键词**：代理化科学, 科学工作流基础设施, AI for Science, 可追溯执行, 生态系统构建, 大规模编排

## 3 点简述
- 核心问题：大规模代理化科学面临工作流难以观察、工具不兼容、执行难追溯和系统定制化限制等问题。
- 方法要点：Bohrium作为AI4S资产中心，将科学资源转化为代理就绪能力；SciMaster编排长视野工作流，支持代理组合与执行。
- 实验或效果：在真实工作流中部署11个主代理，实现端到端科学周期时间数量级减少，并生成大规模执行信号。

## 摘要（原文）

> AI agents are emerging as a practical way to run multi-step scientific workflows that interleave reasoning with tool use and verification, pointing to a shift from isolated AI-assisted steps toward \emph{agentic science at scale}. This shift is increasingly feasible, as scientific tools and models can be invoked through stable interfaces and verified with recorded execution traces, and increasingly necessary, as AI accelerates scientific output and stresses the peer-review and publication pipeline, raising the bar for traceability and credible evaluation.
>   However, scaling agentic science remains difficult: workflows are hard to observe and reproduce; many tools and laboratory systems are not agent-ready; execution is hard to trace and govern; and prototype AI Scientist systems are often bespoke, limiting reuse and systematic improvement from real workflow signals.
>   We argue that scaling agentic science requires an infrastructure-and-ecosystem approach, instantiated in Bohrium+SciMaster. Bohrium acts as a managed, traceable hub for AI4S assets -- akin to a HuggingFace of AI for Science -- that turns diverse scientific data, software, compute, and laboratory systems into agent-ready capabilities. SciMaster orchestrates these capabilities into long-horizon scientific workflows, on which scientific agents can be composed and executed. Between infrastructure and orchestration, a \emph{scientific intelligence substrate} organizes reusable models, knowledge, and components into executable building blocks for workflow reasoning and action, enabling composition, auditability, and improvement through use.
>   We demonstrate this stack with eleven representative master agents in real workflows, achieving orders-of-magnitude reductions in end-to-end scientific cycle time and generating execution-grounded signals from real workloads at multi-million scale.

