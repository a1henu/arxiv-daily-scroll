---
layout: default
title: WISE: A Multimodal Search Engine for Visual Scenes, Audio, Objects, Faces, Speech, and Metadata
---

# WISE: A Multimodal Search Engine for Visual Scenes, Audio, Objects, Faces, Speech, and Metadata
**arXiv**：[2602.12819v1](https://arxiv.org/abs/2602.12819) · [PDF](https://arxiv.org/pdf/2602.12819.pdf)  
**作者**：Prasanna Sridhar, Horace Lee, David M. S. Pinto, Andrew Zisserman, Abhishek Dutta  

**一句话要点**：提出WISE多模态搜索引擎，集成视觉、音频、语音和元数据检索，支持非专家用户高效查询大规模多媒体数据。

**关键词**：多模态检索, 向量搜索, 开源工具, 大规模数据, 模块化架构

## 3 点简述
- 核心问题：如何为缺乏机器学习经验的用户提供统一的多模态检索工具，覆盖图像、视频、音频、人脸、语音和元数据查询。
- 方法要点：采用向量搜索技术，支持自然语言、反向图像、音频文件和元数据过滤，模块化架构便于集成新模型。
- 实验或效果：可扩展至百万图像或千小时视频，已应用于真实场景，代码开源支持本地部署。

## 摘要（原文）

> In this paper, we present WISE, an open-source audiovisual search engine which integrates a range of multimodal retrieval capabilities into a single, practical tool accessible to users without machine learning expertise. WISE supports natural-language and reverse-image queries at both the scene level (e.g. empty street) and object level (e.g. horse) across images and videos; face-based search for specific individuals; audio retrieval of acoustic events using text (e.g. wood creak) or an audio file; search over automatically transcribed speech; and filtering by user-provided metadata. Rich insights can be obtained by combining queries across modalities -- for example, retrieving German trains from a historical archive by applying the object query "train" and the metadata query "Germany", or searching for a face in a place. By employing vector search techniques, WISE can scale to support efficient retrieval over millions of images or thousands of hours of video. Its modular architecture facilitates the integration of new models. WISE can be deployed locally for private or sensitive collections, and has been applied to various real-world use cases. Our code is open-source and available at https://gitlab.com/vgg/wise/wise.

