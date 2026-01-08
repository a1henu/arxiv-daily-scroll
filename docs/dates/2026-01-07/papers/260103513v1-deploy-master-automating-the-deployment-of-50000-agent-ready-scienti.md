---
layout: default
title: Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day
---

# Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day
**arXiv**：[2601.03513v1](https://arxiv.org/abs/2601.03513) · [PDF](https://arxiv.org/pdf/2601.03513.pdf)  
**作者**：Yi Wang, Zhenting Huang, Zhaohan Ding, Ruoxue Liao, Yuan Huang, Xinzijian Liu, Jiajun Xie, Siheng Chen, Linfeng Zhang  

**一句话要点**：提出Deploy-Master自动化部署5万+科学工具，解决开源软件部署瓶颈以支持AI4S和代理工作流。

**关键词**：科学工具部署, 自动化构建, 容器化执行, AI4S工作流, 大规模验证

## 3 点简述
- 核心问题：开源科学软件部署困难，限制可重复性、大规模评估及AI4S集成。
- 方法要点：基于分类学大规模发现工具，通过构建推断和基于执行的验证实现容器化部署。
- 实验或效果：一天内完成5万余构建尝试，成功部署5万余工具，并分析大规模部署的吞吐、成本和失败模式。

## 摘要（原文）

> Open-source scientific software is abundant, yet most tools remain difficult to compile, configure, and reuse, sustaining a small-workshop mode of scientific computing. This deployment bottleneck limits reproducibility, large-scale evaluation, and the practical integration of scientific tools into modern AI-for-Science (AI4S) and agentic workflows.
>   We present Deploy-Master, a one-stop agentic workflow for large-scale tool discovery, build specification inference, execution-based validation, and publication. Guided by a taxonomy spanning 90+ scientific and engineering domains, our discovery stage starts from a recall-oriented pool of over 500,000 public repositories and progressively filters it to 52,550 executable tool candidates under license- and quality-aware criteria. Deploy-Master transforms heterogeneous open-source repositories into runnable, containerized capabilities grounded in execution rather than documentation claims. In a single day, we performed 52,550 build attempts and constructed reproducible runtime environments for 50,112 scientific tools. Each successful tool is validated by a minimal executable command and registered in SciencePedia for search and reuse, enabling direct human use and optional agent-based invocation.
>   Beyond delivering runnable tools, we report a deployment trace at the scale of 50,000 tools, characterizing throughput, cost profiles, failure surfaces, and specification uncertainty that become visible only at scale. These results explain why scientific software remains difficult to operationalize and motivate shared, observable execution substrates as a foundation for scalable AI4S and agentic science.

