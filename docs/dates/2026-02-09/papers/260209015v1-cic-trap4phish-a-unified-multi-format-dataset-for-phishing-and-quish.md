---
layout: default
title: CIC-Trap4Phish: A Unified Multi-Format Dataset for Phishing and Quishing Attachment Detection
---

# CIC-Trap4Phish: A Unified Multi-Format Dataset for Phishing and Quishing Attachment Detection
**arXiv**：[2602.09015v1](https://arxiv.org/abs/2602.09015) · [PDF](https://arxiv.org/pdf/2602.09015.pdf)  
**作者**：Fatemeh Nejati, Mahdi Rabbani, Mansur Mirani, Gunjan Piya, Igor Opushnyev, Ali A. Ghorbani, Sajjad Dadkhah  

**一句话要点**：提出CIC-Trap4Phish统一多格式数据集，用于钓鱼和二维码钓鱼附件检测。

**关键词**：钓鱼攻击检测, 多格式数据集, 静态特征提取, 轻量级机器学习, 二维码钓鱼检测, 特征选择

## 3 点简述
- 钓鱼攻击常通过恶意邮件附件传播，现有数据集缺乏统一性和全面性。
- 构建包含Word、Excel、PDF、HTML和QR码的多格式数据集，提出静态特征提取管道。
- 使用轻量级机器学习模型评估特征，实现高检测准确率，并针对二维码钓鱼采用CNN和语言模型方法。

## 摘要（原文）

> Phishing attacks represents one of the primary attack methods which is used by cyber attackers. In many cases, attackers use deceptive emails along with malicious attachments to trick users into giving away sensitive information or installing malware while compromising entire systems. The flexibility of malicious email attachments makes them stand out as a preferred vector for attackers as they can embed harmful content such as malware or malicious URLs inside standard document formats. Although phishing email defenses have improved a lot, attackers continue to abuse attachments, enabling malicious content to bypass security measures. Moreover, another challenge that researches face in training advance models, is lack of an unified and comprehensive dataset that covers the most prevalent data types. To address this gap, we generated CIC-Trap4Phish, a multi-format dataset containing both malicious and benign samples across five categories commonly used in phishing campaigns: Microsoft Word documents, Excel spreadsheets, PDF files, HTML pages, and QR code images. For the first four file types, a set of execution-free static feature pipeline was proposed, designed to capture structural, lexical, and metadata-based indicators without the need to open or execute files. Feature selection was performed using a combination of SHAP analysis and feature importance, yielding compact, discriminative feature subsets for each file type. The selected features were evaluated by using lightweight machine learning models, including Random Forest, XGBoost, and Decision Tree. All models demonstrate high detection accuracy across formats. For QR code-based phishing (quishing), two complementary methods were implemented: image-based detection by employing Convolutional Neural Networks (CNNs) and lexical analysis of decoded URLs using recent lightweight language models.

