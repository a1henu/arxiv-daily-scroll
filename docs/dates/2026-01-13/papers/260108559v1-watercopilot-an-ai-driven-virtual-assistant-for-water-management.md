---
layout: default
title: WaterCopilot: An AI-Driven Virtual Assistant for Water Management
---

# WaterCopilot: An AI-Driven Virtual Assistant for Water Management
**arXiv**：[2601.08559v1](https://arxiv.org/abs/2601.08559) · [PDF](https://arxiv.org/pdf/2601.08559.pdf)  
**作者**：Keerththanan Vickneswaran, Mariangel Garcia Andarcia, Hugo Retief, Chris Dickens, Paulo Silva  

**一句话要点**：提出WaterCopilot AI虚拟助手，以解决跨界河流流域水资源管理中的数据碎片化和实时访问难题。

**关键词**：水资源管理, 检索增强生成, 虚拟助手, 跨界河流, 实时数据集成, AI驱动决策

## 3 点简述
- 核心问题：跨界河流流域水资源管理面临数据碎片化、实时访问有限和信息整合复杂等挑战。
- 方法要点：基于检索增强生成和工具调用架构，集成静态政策文档与实时水文数据，通过自定义插件实现语义搜索和动态查询。
- 实验或效果：使用RAGAS框架评估，总体得分0.8043，答案相关性0.8571，上下文精确度0.8009，支持多语言交互和可视化。

## 摘要（原文）

> Sustainable water resource management in transboundary river basins is challenged by fragmented data, limited real-time access, and the complexity of integrating diverse information sources. This paper presents WaterCopilot-an AI-driven virtual assistant developed through collaboration between the International Water Management Institute (IWMI) and Microsoft Research for the Limpopo River Basin (LRB) to bridge these gaps through a unified, interactive platform. Built on Retrieval-Augmented Generation (RAG) and tool-calling architectures, WaterCopilot integrates static policy documents and real-time hydrological data via two custom plugins: the iwmi-doc-plugin, which enables semantic search over indexed documents using Azure AI Search, and the iwmi-api-plugin, which queries live databases to deliver dynamic insights such as environmental-flow alerts, rainfall trends, reservoir levels, water accounting, and irrigation data. The system features guided multilingual interactions (English, Portuguese, French), transparent source referencing, automated calculations, and visualization capabilities. Evaluated using the RAGAS framework, WaterCopilot achieves an overall score of 0.8043, with high answer relevancy (0.8571) and context precision (0.8009). Key innovations include automated threshold-based alerts, integration with the LRB Digital Twin, and a scalable deployment pipeline hosted on AWS. While limitations in processing non-English technical documents and API latency remain, WaterCopilot establishes a replicable AI-augmented framework for enhancing water governance in data-scarce, transboundary contexts. The study demonstrates the potential of this AI assistant to support informed, timely decision-making and strengthen water security in complex river basins.

