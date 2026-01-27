---
layout: default
title: MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs
---

# MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs
**arXiv**：[2601.18113v1](https://arxiv.org/abs/2601.18113) · [PDF](https://arxiv.org/pdf/2601.18113.pdf)  
**作者**：Dezhang Kong, Zhuxi Wu, Shiqi Liu, Zhicheng Tan, Kuichen Lu, Minghao Li, Qichen Liu, Shengyu Chu, Zhenhua Xu, Xuan Liu, Meng Han  

**一句话要点**：提出MalURLBench基准以评估LLM处理恶意URL时的漏洞，并设计URLGuard防御模块。

**关键词**：恶意URL检测, LLM安全基准, Web代理漏洞, URLGuard防御, 攻击实例评估

## 3 点简述
- 核心问题：LLM代理在处理恶意URL时存在严重漏洞，可能导致访问不安全网页，但缺乏针对性基准。
- 方法要点：构建包含61,845个攻击实例的基准，覆盖10个真实场景和7类恶意网站，并分析关键攻击因素。
- 实验或效果：测试12个流行LLM，发现模型难以检测伪装恶意URL，提出轻量级防御模块URLGuard。

## 摘要（原文）

> LLM-based web agents have become increasingly popular for their utility in daily life and work. However, they exhibit critical vulnerabilities when processing malicious URLs: accepting a disguised malicious URL enables subsequent access to unsafe webpages, which can cause severe damage to service providers and users. Despite this risk, no benchmark currently targets this emerging threat. To address this gap, we propose MalURLBench, the first benchmark for evaluating LLMs' vulnerabilities to malicious URLs. MalURLBench contains 61,845 attack instances spanning 10 real-world scenarios and 7 categories of real malicious websites. Experiments with 12 popular LLMs reveal that existing models struggle to detect elaborately disguised malicious URLs. We further identify and analyze key factors that impact attack success rates and propose URLGuard, a lightweight defense module. We believe this work will provide a foundational resource for advancing the security of web agents. Our code is available at https://github.com/JiangYingEr/MalURLBench.

