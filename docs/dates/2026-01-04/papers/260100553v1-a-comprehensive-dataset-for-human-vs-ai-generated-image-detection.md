---
layout: default
title: A Comprehensive Dataset for Human vs. AI Generated Image Detection
---

# A Comprehensive Dataset for Human vs. AI Generated Image Detection
**arXiv**：[2601.00553v1](https://arxiv.org/abs/2601.00553) · [PDF](https://arxiv.org/pdf/2601.00553.pdf)  
**作者**：Rajarshi Roy, Nasrin Imanpour, Ashhar Aziz, Shashwat Bajpai, Gurpreet Singh, Shwetangshu Biswas, Kapil Wanaskar, Parth Patwa, Subhankar Ghosh, Shreyas Dixit, Nilesh Ranjan Pal, Vipula Rawte, Ritvik Garimella, Gaytri Jena, Vasu Sharma, Vinija Jain, Aman Chadha, Aishwarya Naresh Reganti, Amitava Das  

**一句话要点**：提出MS COCOAI数据集以解决AI生成图像检测的挑战

**关键词**：AI生成图像检测, 合成数据集, 多模态生成AI, 图像分类, 模型识别

## 3 点简述
- 核心问题：生成式AI图像难以与真实照片区分，导致误导内容传播
- 方法要点：基于MS COCO构建包含96000个真实与合成数据点的数据集，使用五种生成器
- 实验或效果：支持图像真伪分类和生成模型识别任务，数据集已公开可用

## 摘要（原文）

> Multimodal generative AI systems like Stable Diffusion, DALL-E, and MidJourney have fundamentally changed how synthetic images are created. These tools drive innovation but also enable the spread of misleading content, false information, and manipulated media. As generated images become harder to distinguish from photographs, detecting them has become an urgent priority. To combat this challenge, We release MS COCOAI, a novel dataset for AI generated image detection consisting of 96000 real and synthetic datapoints, built using the MS COCO dataset. To generate synthetic images, we use five generators: Stable Diffusion 3, Stable Diffusion 2.1, SDXL, DALL-E 3, and MidJourney v6. Based on the dataset, we propose two tasks: (1) classifying images as real or generated, and (2) identifying which model produced a given synthetic image. The dataset is available at https://huggingface.co/datasets/Rajarshi-Roy-research/Defactify_Image_Dataset.

