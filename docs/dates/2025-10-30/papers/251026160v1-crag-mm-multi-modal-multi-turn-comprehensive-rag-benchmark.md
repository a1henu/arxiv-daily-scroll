---
layout: default
title: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
---

# CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
**arXiv**：[2510.26160v1](https://arxiv.org/abs/2510.26160) · [PDF](https://arxiv.org/pdf/2510.26160.pdf)  
**作者**：Jiaqi Wang, Xiao Yang, Kai Sun, Parth Suresh, Sanat Sharma, Adam Czyzewski, Derek Andersen, Surya Appini, Arkav Banerjee, Sajal Choudhary, Shervin Ghasemlou, Ziqiang Guan, Akil Iyer, Haidar Khan, Lingkun Kong, Roy Luo, Tiffany Ma, Zhen Qiao, David Tran, Wenfang Xu, Skyler Yeatman, Chen Zhou, Gunveer Gujral, Yinglong Xia, Shane Moon, Nicolas Scheffer, Nirav Shah, Eun Chang, Yue Liu, Florian Metze, Tammy Stark, Zhaleh Feizollahi, Andrea Jessee, Mangesh Pujari, Ahmed Aly, Babak Damavandi, Rakesh Wanga, Anuj Kumar, Rohit Patel, Wen-tau Yih, Xin Luna Dong  

**一句话要点**：提出CRAG-MM基准以评估可穿戴场景下的多模态多轮RAG系统

**关键词**：多模态检索增强生成, 可穿戴设备基准, 多轮对话评估, 图像知识图谱检索, 真实世界场景模拟

## 3 点简述
- 核心问题：缺乏针对可穿戴设备的多模态多轮检索增强生成综合基准
- 方法要点：构建包含6.5K三元组和2K多轮对话的数据集，覆盖13个领域
- 实验或效果：基线方法真实度仅32-43%，显示改进空间，已用于KDD Cup 2025

## 摘要（原文）

> Wearable devices such as smart glasses are transforming the way people
> interact with their surroundings, enabling users to seek information regarding
> entities in their view. Multi-Modal Retrieval-Augmented Generation (MM-RAG)
> plays a key role in supporting such questions, yet there is still no
> comprehensive benchmark for this task, especially regarding wearables
> scenarios. To fill this gap, we present CRAG-MM -- a Comprehensive RAG
> benchmark for Multi-modal Multi-turn conversations. CRAG-MM contains a diverse
> set of 6.5K (image, question, answer) triplets and 2K visual-based multi-turn
> conversations across 13 domains, including 6.2K egocentric images designed to
> mimic captures from wearable devices. We carefully constructed the questions to
> reflect real-world scenarios and challenges, including five types of
> image-quality issues, six question types, varying entity popularity, differing
> information dynamism, and different conversation turns. We design three tasks:
> single-source augmentation, multi-source augmentation, and multi-turn
> conversations -- each paired with an associated retrieval corpus and APIs for
> both image-KG retrieval and webpage retrieval. Our evaluation shows that
> straightforward RAG approaches achieve only 32% and 43% truthfulness on CRAG-MM
> single- and multi-turn QA, respectively, whereas state-of-the-art industry
> solutions have similar quality (32%/45%), underscoring ample room for
> improvement. The benchmark has hosted KDD Cup 2025, attracting about 1K
> participants and 5K submissions, with winning solutions improving baseline
> performance by 28%, highlighting its early impact on advancing the field.

